##This was developed for fun when I was playing a video game.
##This was during my first few months in CTI-110.

#Elden Ring - MaxLoadCalc
#Determines how much max load you need for your current equip load.
#You can pick which weight class you'd like to fall under.


equip_load = float(input("What is your equip load? "))
u_max_load = float(input("What is your current max load? "))
desired_weight_class = input("\nEnter your desired weight class.\n(light, mid, heavy, or overeloaded): ").strip().lower()

if desired_weight_class not in ['light', 'mid', 'heavy', 'overloaded']:
    print("Invalid weight classs. Please enter a valid weight class.")
else:
    if desired_weight_class == 'light':
        max_load = equip_load / 0.299
    elif desired_weight_class == 'mid':
        max_load = equip_load / 0.699
    elif desired_weight_class == 'heavy':
        max_load = equip_load / 0.999
    else:
        max_load = equip_load / 1.01 #Slightly over 100% for overloaded

    print(f"\nTo maintain a '{desired_weight_class}' weight class, your maximum load should be at least {max_load:.2f}.")
    print(f"Your current max load is: {u_max_load:.2f}.")
