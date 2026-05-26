# Rental Calculator
print("Let's try a Rent Calculator")
rent = int(input("Enter the rental amount : "))
units = int(input("Enter the no. of units spent : ")) 
charge = int(input("Enter the charge per unit for electricity : "))
member = int(input("Enter the no. of members for Rent diivision : "))

pay =round((rent +(units*charge))/member,2)
print(f"Each person has to pay : {pay}")



