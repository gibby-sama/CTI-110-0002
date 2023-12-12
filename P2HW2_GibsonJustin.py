# CTI-110-002
# P2HW2 - Module Grading List
# Justin Gibson
# September 19, 2023

## **************************** Pseudocode *************************************
## Create input float variables for modules 1-6
## Create a list called modlist for each of the 6 modules
## Make a variable fore min, max, sum and average of modlist
## Print results for lowest grade, highest grade, sum & average of modlist
## Display lowest grade, highest grade, and sum with 1 decimal point
## Display average with 2 decimal points
## Decimal points are displayed this way to match the output in the assignment example

mod1 = float(input('Enter grade for Module 1: '))
mod2 = float(input('Enter grade for Module 2: '))
mod3 = float(input('Enter grade for Module 3: '))
mod4 = float(input('Enter grade for Module 4: '))
mod5 = float(input('Enter grade for Module 5: '))
mod6 = float(input('Enter grade for Module 6: '))

modlist = [ mod1, mod2, mod3, mod4, mod5, mod6 ]
min_g = min(modlist)
max_g = max(modlist)
sum_g = sum(modlist)
avg_g = sum(modlist) / len(modlist)

print()
print('-----------------Results----------------------')
print(f'Lowest Grade:   {min_g: .1f}')
print(f'Highest Grade:  {max_g: .1f}')
print(f'Sum of Grades:  {sum_g: .1f}')
print(f'Average:        {avg_g: .2f}')
print('----------------------------------------------')

