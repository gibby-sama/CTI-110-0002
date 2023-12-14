##This is a cost calculator for the video game Genshin Impact
##Another code I made for fun in the first few months of CTI-110

gachaRoll = 160

# Create a dictionary to map the user's input to the corresponding values
pack_values = {
    '1A': {'primos': 120, 'cost': 0.99, 'rolls': 0.75},
    '2A': {'primos': 600, 'cost': 4.99, 'rolls': 3.75},
    '3A': {'primos': 1960, 'cost': 14.99, 'rolls': 12.25},
    '4A': {'primos': 3960, 'cost': 29.99, 'rolls': 24.75},
    '5A': {'primos': 6560, 'cost': 49.99, 'rolls': 41},
    '6A': {'primos': 12960, 'cost': 99.99, 'rolls': 81},
    
    '1B': {'primos': 60, 'cost': 0.99}, 'rolls': 0.375,
    '2B': {'primos': 330, 'cost': 4.99, 'rolls': 2.0625},
    '3B': {'primos': 1090, 'cost': 14.99, 'rolls': 6.8125},
    '4B': {'primos': 2240, 'cost': 29.99, 'rolls': 14},
    '5B': {'primos': 3880, 'cost': 49.99, 'rolls': 24.25},
    '6B': {'primos': 8080, 'cost': 99.99, 'rolls': 50.5},
}

print("""|Genshin Calculator|
Total rolls/cost for top-up packs.
==============================================
First-time top-up packs:
1A. 60+60 (120)      | $0.99  | 0.75 rolls
2A. 300+300 (600)    | $4.99  | 3.75 rolls
3A. 980+980 (1960)   | $14.99 | 12.25 rolls
4A. 1980+1980 (3960) | $29.99 | 24.75 rolls
5A. 3280+3280 (6560) | $49.99 | 41 rolls
6A. 6480+6480 (12960)| $99.99 | 81 rolls

Regular top-up packs:
1B. 60               | $0.99  | 0.375 rolls
2B. 300+30 (330)     | $4.99  | 2.0625 rolls
3B. 980+110 (1090)   | $14.99 | 6.8125 rolls
4B. 1980+260 (2240)  | $29.99 | 14 rolls
5B. 3280+600 (3880)  | $49.99 | 24.25 rolls
6B. 6480+1600 (8080) | $99.99 | 50.5 rolls
==============================================""")

num_packs = int(input("How many packs will you buy? "))
pack_list = []


for i in range(num_packs):
    while True:
        buy_pack = input(f'Enter pack #{i+1}: ')
        if buy_pack in pack_values:
            pack_list.append(buy_pack)
            break
        else:    
            print("Please enter a valid input.")

total_primos = sum(pack_values[pack]['primos'] for pack in pack_list)
total_cost = sum(pack_values[pack]['cost'] for pack in pack_list)
o_rolls = total_primos / gachaRoll

print(f"""----------------------------------------------
Total primogems obtained: {total_primos}
Total cost: ${total_cost}
Number of rolls: {o_rolls:.2f}""")



##1. gachaRoll = 160: This line initializes a variable gachaRoll with
##the value 160, which is the number of Primogems needed for one gacha roll in the game.
##
##2. pack_values is a dictionary that stores information about the packs available for purchase.
##Each pack is represented by a unique code, and for each pack code, it contains two pieces of information:
##    'primos': The number of Primogems you receive when you purchase that pack.
##    'cost': The cost of the pack in USD.
##
##3. The code then prints a welcome message and displays the details of the available packs using a multi-line string.
##    num_packs = int(input("How many packs will you buy? ")):
##    This line asks the user how many packs they want to purchase and stores the user's input as an integer in the num_packs variable.
##
##5. pack_list = []: This initializes an empty list called pack_list to store the pack codes that the user inputs.
##
##6. The following loop, which starts with for i in range(num_packs):, allows the user to input the pack codes they want to buy. It iterates num_packs times, and for each iteration:
##    buy_pack = input(f'Enter pack #{i+1}: '): It asks the user to enter the code for the pack they want to purchase. The entered pack code is stored in the buy_pack variable.
##    if buy_pack in pack_values:: It checks if the entered buy_pack is a valid key in the pack_values dictionary.
##    If the entered pack code is valid, it appends the pack code to the pack_list using pack_list.append(buy_pack).
##    If the entered pack code is not valid, it displays an error message and asks the user to enter a valid input. The loop continues until the user enters a valid pack code.
##
##7. After the loop, the code calculates the total Primogems obtained and the total cost of the packs based on the user's input.
##It uses list comprehensions to extract the information from the pack_values dictionary for each pack in pack_list.
##
##8.Finally, it calculates the number of rolls the user gets based on the total Primogems obtained, and it prints the results, including the total Primogems, total cost, and number of rolls.
##This code essentially allows the user to input the packs they want to purchase, and it calculates the total Primogems obtained, total cost, and the number of rolls they can get from those packs.

