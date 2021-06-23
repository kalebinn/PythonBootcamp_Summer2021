import random 


print("Press 1 to spin the slot machine")
print("Press anything else to walk away")
user_input = input("Enter your choice: ")

possibilities = ['lemon', 'cherry', 'watermelon', 'lime', 'peach', 'JACKPOT', 'apple', 'orange']
number_of_strips = 3

while user_input == '1':
    user_won = True
    outcomes = random.choices(possibilities, k=number_of_strips)

    print("\n----------------------------------------------")
    for strip in range(0, number_of_strips):
        print(f'| {outcomes[strip]} |', end="")
    print("\n----------------------------------------------")

    # we need to check if the user won!  
    for strip in range(0, number_of_strips):
        if outcomes[strip] != 'JACKPOT':
            user_won = False
    
    if user_won == True:
        print("YOU WON THE JACKPOT")

    print("\nPress 1 to play again")
    print("Press anything else to walk away")
    user_input = input("Enter your choice: ")

    if user_input != '1':
        print("Goodbye. Thank you for playing.")



