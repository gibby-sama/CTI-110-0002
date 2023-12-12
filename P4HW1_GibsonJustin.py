# CTI-110-002
# P4HW1 - Grading Loop
# Justin Gibson
# November 2, 2023

## **************************** Pseudocode *************************************
# This is a Python program that uses a loop to create a grade list.
# 1. Ask user to input how many times they want the 'for loop' to run.
#    "How many scores would you like to enter?"
# 2. Create an empty list called 'grade_list' that stores each grade.
# 3. Ask user "Enter Score #1, 2, 3, etc." based on how many times they've run the loop.
# 3-1. If score is greater or equal to 0, ask for the next score.
# 3-2. If the score is less than 0, tell user to input a different number.
#      And enter #_ again.
# 4. Make sure all scores entered are stored into grade_list

#works properly, but doesn't tell user to 'enter score #_ again:'.
#it just repeats 'enter score #_'
num_scores = int(input("How many scores would you like to enter? "))
print()

grade_list = []

for i in range(num_scores):
    score = float(input(f'Enter score #{i + 1 }: '))
    while True:
        
        
        if score < 0:
            print()
            print('INVALID Score entered!!!!')
            print('Score should be between 0 and 100')
            score = float(input(f'Enter score #{i + 1 } again: '))
            # Need to enter an input that'll say "Enter #_ again: "
        else:
            grade_list.append(score)
            break

###ignore this for grading. It was just me trying different loop structures.###
##if the user enters a negative nummber twice, the 2nd number will be stored in grade_list
##num_scores = int(input("How many scores would you like to enter? "))
##print()
##
##grade_list = []
##
##for i in range(num_scores):
##    score = float(input(f'Enter score #{i + 1}: '))
##
##    if score >= 0:
##        grade_list.append(score)
##
##    elif score < 0:
##        print()
##        print('INVALID Score entered!!!!')
##        print('Score should be between 0 and 100')
##        score = float(input(f'Enter score #{i + 1} again: '))
##        grade_list.append(score)
###


#remove lowest grade
mod_list = [num for num in grade_list if num != min(grade_list)]
##This part REALLY confused me
##Essentially the code is saying:
##Go number by number in grade_list & copy it to mod_list,
##as long as the number is not the lowest number within grade_list
##So. It'll copy every number from grade_list to mod_list, except min(grade_list)

min_g = min(grade_list)
max_g = max(grade_list)
sum_g = sum(grade_list)
avg_g = sum(grade_list) / len(grade_list)

avg_g2 = sum(mod_list) / len(mod_list)

#elif statement to determine letter grade
if avg_g >= 90:
    f_grade = 'A'
elif avg_g >= 80:
    f_grade = 'B'
elif avg_g >= 70:
    f_grade = 'C'
elif avg_g >= 60:
    f_grade = 'D'
elif avg_g <= 59:
    f_grade = 'F'

    
#Need some formatting help
#Also, the average score on the assignment is wrong
print()
print('-----------------Results----------------------')
print(f'Lowest Score  : {min_g: .1f}')
print(f'Modified List :  {mod_list}')
print(f'Scores Average: {avg_g2: .2f}')
print(f'Grade         :  {f_grade}')
print('----------------------------------------------')

