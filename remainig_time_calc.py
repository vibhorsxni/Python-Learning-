# Time Calculator 
print(f"-----Let's calculate the remaining Time ⌚ i.e remaining Hour, Minutes and Seconds of the Day ------")
time = input("Enter the current time in 24 hour format (HH:MM:SS): ")
spent = int(time[0:2])*3600 + int(time[3:5])*60 + int(time[6:8])
remaining = 24*3600 - spent
remaining_hours = remaining // 3600
remaining_minutes = (remaining % 3600) // 60
remaining_seconds = (remaining % 3600) % 60
print(f"----------------Remaining Time of the day -> {remaining_hours}:{remaining_minutes}:{remaining_seconds}-------------------") 
print(f'''Remaining Hours : {remaining_hours} Hours
Remaining Minutes : {remaining_minutes} Minutes
Remaining Seconds : {remaining_seconds} Seconds''' )