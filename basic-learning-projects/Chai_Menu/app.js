/* ═══════════════════════════════════════════════════
   Sharmili Chai — Application Logic
   Mirrors practice.py ordering flow in the browser
   ═══════════════════════════════════════════════════ */

// ── Data (mirroring practice.py) ──
const menu = [
  { id: "1", name: "Masala Chai",    emoji: "☕",  price: 20, color: "#c5884d" },
  { id: "2", name: "Ginger Chai",    emoji: "🫖",  price: 30, color: "#d4a76a" },
  { id: "3", name: "Cardamom Chai",  emoji: "🌿",  price: 30, color: "#8db87c" },
  { id: "4", name: "Green Tea",      emoji: "🍵",  price: 40, color: "#7dbf91" },
  { id: "5", name: "Bubble Tea",     emoji: "🧋",  price: 60, color: "#c78dba" },
];

const addons = [
  { id: "1", name: "Extra Sugar", emoji: "🍬", price: 2  },
  { id: "2", name: "Rusk",        emoji: "🍪", price: 5  },
  { id: "3", name: "Bread",       emoji: "🍞", price: 5  },
];

// ── State ──
let selectedTea   = null;
let selectedAddon = null;

// ── DOM refs ──
const menuGrid     = document.getElementById("menu-grid");
const addonsGrid   = document.getElementById("addons-grid");
const addonsSection = document.getElementById("addons-section");
const billSection  = document.getElementById("bill-section");
const receiptItems = document.getElementById("receipt-items");
const receiptTotal = document.getElementById("receipt-total");

// ══════════════════════════
// Render Menu Cards
// ══════════════════════════
function renderMenu() {
  menuGrid.innerHTML = menu
    .map(
      (item) => `
    <div class="menu-card" id="tea-${item.id}" onclick="selectTea('${item.id}')">
      <span class="card-emoji">${item.emoji}</span>
      <div class="card-name">${item.name}</div>
      <div class="card-price">₹${item.price} <span>/ cup</span></div>
    </div>`
    )
    .join("");
}

// ══════════════════════════
// Render Add-On Cards
// ══════════════════════════
function renderAddons() {
  addonsGrid.innerHTML = addons
    .map(
      (a) => `
    <div class="addon-card" id="addon-${a.id}" onclick="selectAddon('${a.id}')">
      <span class="addon-emoji">${a.emoji}</span>
      <div class="addon-name">${a.name}</div>
      <div class="addon-price">+ ₹${a.price}</div>
    </div>`
    )
    .join("");
}

// ══════════════════════════
// Selection Handlers
// ══════════════════════════
function selectTea(id) {
  selectedTea = menu.find((t) => t.id === id);

  // Highlight selected card
  document.querySelectorAll(".menu-card").forEach((c) => c.classList.remove("selected"));
  document.getElementById(`tea-${id}`).classList.add("selected");

  // Show add-ons section with animation
  addonsSection.classList.remove("hidden");
  addonsSection.style.animation = "fadeUp 0.5s ease-out both";

  // Scroll smoothly
  setTimeout(() => {
    addonsSection.scrollIntoView({ behavior: "smooth", block: "start" });
  }, 200);
}

function selectAddon(id) {
  selectedAddon = addons.find((a) => a.id === id);

  // Highlight selected card
  document.querySelectorAll(".addon-card").forEach((c) => c.classList.remove("selected"));
  document.getElementById(`addon-${id}`).classList.add("selected");

  // Short delay then show bill
  setTimeout(() => showBill(), 400);
}

function skipAddon() {
  selectedAddon = null;
  showBill();
}

// ══════════════════════════
// Build Receipt
// ══════════════════════════
function showBill() {
  if (!selectedTea) return;

  // Hide add-ons
  addonsSection.classList.add("hidden");

  // Compute total
  const teaPrice   = selectedTea.price;
  const addonPrice = selectedAddon ? selectedAddon.price : 0;
  const total      = teaPrice + addonPrice;

  // Build receipt rows
  let rows = `
    <div class="receipt-row">
      <span>${selectedTea.emoji} ${selectedTea.name}</span>
      <span>₹${teaPrice}</span>
    </div>`;

  if (selectedAddon) {
    rows += `
    <div class="receipt-row">
      <span>${selectedAddon.emoji} ${selectedAddon.name}</span>
      <span>₹${addonPrice}</span>
    </div>`;
  }

  receiptItems.innerHTML = rows;
  receiptTotal.innerHTML = `
    <div class="receipt-row total">
      <span>Total</span>
      <span>₹${total}</span>
    </div>`;

  // Show bill section
  billSection.classList.remove("hidden");
  billSection.style.animation = "fadeUp 0.6s ease-out both";

  setTimeout(() => {
    billSection.scrollIntoView({ behavior: "smooth", block: "center" });
  }, 100);
}

// ══════════════════════════
// Reset / New Order
// ══════════════════════════
function resetOrder() {
  selectedTea   = null;
  selectedAddon = null;

  document.querySelectorAll(".menu-card").forEach((c) => c.classList.remove("selected"));
  document.querySelectorAll(".addon-card").forEach((c) => c.classList.remove("selected"));

  addonsSection.classList.add("hidden");
  billSection.classList.add("hidden");

  document.getElementById("menu-section").scrollIntoView({ behavior: "smooth", block: "start" });
}

// ══════════════════════════
// Smooth scroll from hero
// ══════════════════════════
function scrollToMenu() {
  document.getElementById("menu-section").scrollIntoView({ behavior: "smooth", block: "start" });
}

// ── Init ──
renderMenu();
renderAddons();
