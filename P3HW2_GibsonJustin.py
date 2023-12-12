# Elif Paycheck Calculator (w/ overtime)
# October 12, 2023
# CTI-110-002 P3HW2
# Justin Gibson


## This program calculates an employee's paycheck, including separate columns for overtime hours & pay.
## User is asked to input employee name, hours worked & payrate. The program calculates the rest.

# Ask user to define employee name, hours worked & pay rate. Program stores them into variables.
e_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Create an elif statement to define overtime calculations.
if hours_worked > 40:
    reg_hours = 40
    ot_hours = hours_worked - 40
elif hours_worked <= 40:
    reg_hours = hours_worked
    ot_hours = 0

# Use previously stored variables to define & calculate regular pay, overtime pay & gross pay.
reg_pay = reg_hours * pay_rate
ot_pay = ot_hours * (pay_rate * 1.5)
gross_pay = reg_pay + ot_pay
    
#Display employee name; followed by hours worked, pay rate, overtime hours, overtime pay, regular hours pay & gross pay.  
print("--------------------------------------")
print("Employee name: ", e_name)
print()
print(f'{"Hours worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay"}')
print("-------------------------------------------------------------------------------------")
print(f'{hours_worked:<15.1f}{pay_rate:<12.1f}{ot_hours:<12.1f}{"$"}{ot_pay:<14.2f}{"$"}{reg_pay:<14.2f}{"$"}{gross_pay:.2f}')
