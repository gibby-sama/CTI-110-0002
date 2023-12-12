# Payroll w-Looping Calc
# November 18, 2023
# CTI-110-002 P4HW2
# Justin Gibson


## This program calculates an employee's paycheck, including separate columns for overtime hours & pay.
## User is asked to input employee name, hours worked & payrate. The program calculates the rest.
###This is an updated version that loops & will run the loop until the user enters "Done".

#create variables to store totals from multiple iterations of the while loop.
total_employees = 0
total_ot = 0
total_reg_pay = 0
total_gross_pay = 0


# Ask user to define employee name, hours worked & pay rate. Program stores them into variables.
while True:
    e_name = input("Enter employee's name or 'Done' to terminate: ")

    if e_name == 'Done':
        break

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

    # Updated totals after each loop.
    total_employees += 1
    total_ot += ot_pay
    total_reg_pay += reg_pay
    total_gross_pay += gross_pay


#Display employee name; followed by hours worked, pay rate, overtime hours, overtime pay, regular hours pay & gross pay.  
    print()
    print("Employee name: ", e_name)
    print()
    print(f'{"Hours worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay"}')
    print("-------------------------------------------------------------------------------------")
    print(f'{hours_worked:<15.1f}{pay_rate:<12.1f}{ot_hours:<12.1f}{"$"}{ot_pay:<14.2f}{"$"}{reg_pay:<14.2f}{"$"}{gross_pay:.2f}')
    print()

#Totals after the loop finishes
print()
print(f'Total number of employees entered: {total_employees}')
print(f'Total amount of paid overtime: ${total_ot:.2f}')
print(f'Total amount paid for regular hours: ${total_reg_pay:.2f}')
print(f'Total amount paid in gross: ${total_gross_pay:.2f}')
