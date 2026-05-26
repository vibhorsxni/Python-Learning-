import random 

def ascii_art() :
    print(r'''
█████ █   █ ████  █      ███  █   █ █████ █████    █   █  ███  █   █  ███   ███  █████ █   █ █████ █   █ █████ 
█     ██ ██ █   █ █     █   █  █ █  █     █        ██ ██ █   █ ██  █ █   █ █     █     ██ ██ █     ██  █   █   
████  █ █ █ ████  █     █   █   █   ████  ████     █ █ █ █████ █ █ █ █████ █  ██ ████  █ █ █ ████  █ █ █   █   
█     █   █ █     █     █   █   █   █     █        █   █ █   █ █  ██ █   █ █   █ █     █   █ █     █  ██   █   
█████ █   █ █     █████  ███    █   █████ █████    █   █ █   █ █   █ █   █  ███  █████ █   █ █████ █   █   █   
''')
    
    
def get_employee() : 
    with open('employee.txt','r') as employee :
        x = eval(employee.read())
        return x

def add_employees(name) :
    employees = get_employee()
    employee_id = random.randint(100000,99999999)
    employee_name = name 
    employees[employee_id] = employee_name
    with open ('employee.txt','w') as f :
        f.write(str(employees))
    print(f"{name} added sucessfully with id : {employee_id}\n")

def delete_employee(employee_id) :
    employees = get_employee()
    X = int(employee_id)
    del employees[employee_id]
    with open ('employee.txt','w') as f :
        f.write(str(employees))
    print(f"Employee deleted sucessfully with id : {X}")

