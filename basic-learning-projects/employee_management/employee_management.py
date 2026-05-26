import help
help.ascii_art()
while True :
    
    action = input ("Exit - break OR \nEnter the action - DELETE/ADD/SEE EMPLOYEES :  ")
    if (action == "break") :
        break 
    else :
        if action in ["Add","ADD","add"] :
            name = input("Enter the name of employee : ")
            help.add_employees(name)
            
        elif action in ["DELETE","Delete","delete"] :
            print(help.get_employee())
            id = int(input("Enter the id of thte employee you want to delete : "))
            help.delete_employee(id)
        elif action in ["see","SEE","See"] :
            print("The list of all the employees is : ")
            print(f"{help.get_employee()}\n")
        else :
            print("Enter a valid Input")
        print("-----------------------------------------------------------------------------------------------------------------")

