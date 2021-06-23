# prices: 
Poland_lake_water = 1.00
Kepsi_cola = 1.50
Sunny_E_OJ = 1.50
Alaskan_punch = 1.25
Blue_bull = 2.50
Dr_Salt = 2.00 

user_selection = input("What is your selection? ")

# “You have ordered [Item]. Your total will be [Price].”
# put all the other selections .. 
if user_selection == "A1":
    print(f"You have ordered Poland Lake Water. Your total will be ${Poland_lake_water}")
elif user_selection == "A2":
    print(f"You have ordered Kepsi Cola. Your total will be ${Kepsi_cola}")
elif user_selection == "B2":
    print(f"You have ordered Sunny E Orange Juice. Your total will be ${Sunny_E_OJ}")
else: 
    print("Your selection was invalid.")

