# Travel Budget Calculator
# August 31, 2023
# CTI-110-0002 P1HW2 - Travel Expense
# Justin Gibson
#


## Make a Travel Expense Calculator ##
## Store Budget & expenses (gas, accomodations, food) in float variables ##
## Store Location into a text input variable ##
## Find the end balance by subtracting expenses from the starting budget ##
## Display the outputs for location, budget, gas, accomodations, food & the ending balance ##

print("This program calculates and displays travel expenses.")
print()
Budget = float(input("Enter Budget: "))
print()
Location = input("Enter your travel destination: ")
print()
Gas = float(input("How much do you think you will spend on gas? "))
print()
Acc = float(input("How much do you think you'll spend on accomodation/hotel? "))
print()
Food = float(input("Last, how much do you need for food? "))
Balance = Budget - Gas - Acc - Food

print()
print("------------------Travel Expenses------------------")
print("Location: ", Location)
print("Initial Budget: ", Budget)
print()
print("Fuel: ", Gas)
print("Accomodation: ", Acc)
print("Food: ", Food)
print()
print("Remaining Balance: ", Balance)
