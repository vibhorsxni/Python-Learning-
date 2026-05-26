# Simple Interest Calculator
print ("Let's calculate the Simple Interest")
principal = float(input("Enter the principal amount : "))
rate = float(input("Enter the rate of interest per year(in %): "))
time = float(input("Enter time (in years): "))
interest = (principal * rate * time) / 100
print (f"Total Interest is : {interest} ")
print (f"Total Amount to be paid is : {principal+interest}")
