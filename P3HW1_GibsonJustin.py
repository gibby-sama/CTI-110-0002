# Elif Grade Calc
# October 3, 2023
# CTI-110-002 P3HW1
# Justin Gibson

# This program takes a number grade, determines average and displays letter grade for average.

# Have end-user input grades for six modules
mod1 = float(input('Enter grade for Module 1: '))
mod2 = float(input('Enter grade for Module 2: '))
mod3 = float(input('Enter grade for Module 3: '))
mod4 = float(input('Enter grade for Module 4: '))
mod5 = float(input('Enter grade for Module 5: '))
mod6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [ mod1, mod2, mod3, mod4, mod5, mod6 ]

#Define variables
len1 = len(grades)

low = min(grades)
high = max(grades)
sum1 = sum(grades)
avg = sum1 / len1

# Output Results for lowest grade, highest grade, sum and average
# Then use elif to display the letter grade for the average of input grades
print('---------Results---------')
print(f'Lowest Grade:   {low: .1f}')
print(f'Highest Grade:  {high: .1f}')
print(f'Sum of Grades:  {sum1: .1f}')
print(f'Average:        {avg: .2f}')
print('------------------------')
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
elif avg <= 59:
    print('Your grade is: F')
