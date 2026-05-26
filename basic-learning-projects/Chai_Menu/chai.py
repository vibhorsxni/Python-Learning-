print ("      ------------Sharmili Chai------------ ")
print ("----------- Special Edition Chai By Sher -----------")
menu = { "1" : 20, "2" : 30, "3" : 30, "4" : 40, "5" : 60 }
print (f'''\n----------------------Chai Menu----------------------------
              1. Masala Chai ☕ - Rs {menu["1"]}
              2. Ginger Chai 🫖 - Rs {menu["2"]}
              3. Cardamom Chai 🌿 - Rs {menu["3"]}
              4. Green Tea 🍵 - Rs {menu["4"]}
              5. Bubble Tea 🧋 - Rs {menu["5"]} ''')

tea = input("\n\nEnter the number corresponding to the tea you want to order : ")

if (tea > "5" or tea < "1") :
    print("Please enter a valid number from the menu")

else :
    amount = int(tea)  
    add = { "1" : 2, "2" : 5, "3" : 5 }
    print(f'''\n ----------------------------Additional Menu----------------------------
           Extra Sugar = 2 Rs
           Need Rusk = 5 Rs
           Need Bread = 5 Rs''')
    add_on = input("\nDo you want to add any of the above items ? (yes/no) : ")
    if (add_on == "yes") :
              add_item = input("Enter the item you want to add (Sugar/Rusk/Bread) : ")
              if (add_item == "Sugar") :
                     bill = menu[tea]+add["1"]
                     print(f"Your total bill is : {bill} Rs")
              elif (add_item == "Rusk") :
                     bill = menu[tea]+add["2"]
                     print(f"Your total bill is : {bill} Rs")
              elif (add_item == "Bread") :
                     bill = menu[tea]+add["3"]
                     print(f"Your total bill is : {bill} Rs")
              else:
                     print("Please enter a valid item from the additional menu")
    else:   
              print(f"Your total bill is : {menu[tea]} Rs")
