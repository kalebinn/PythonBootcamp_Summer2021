# version 1: allow the USER to pick an option. After the user picks an option, display the price of that item 
chicken_sandwich_price = 7.99
McWhopper_price = 5.99 
fries_price = 2.99 

print("1 - Chicken Sandwich")
print("2 - McWhopper")
print("3 - Fries")

user_selection = input("Whatcha want? ")

if user_selection == '1':
    print(f"Your total is: ${chicken_sandwich_price}")
elif user_selection == '2':
    print(f"Your total is: ${McWhopper_price}")
elif user_selection == '3':
    print(f"Your total is: ${fries_price}")
else:
    print("This is an invalid choice, dude")

