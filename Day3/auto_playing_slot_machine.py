import random 


possibilities = ['lemon', 'cherry', 'watermelon', 'lime', 'peach', 'JACKPOT', 'apple', 'orange']
number_of_strips = 5
number_of_plays = 100000
number_of_wins = 0


for play in range(0, number_of_plays):
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
        number_of_wins = number_of_wins + 1 
        print("YOU WON THE JACKPOT")

print(f"We won {number_of_wins} times out of {number_of_plays}")
print(f"Estimated probability of winning: {number_of_wins/number_of_plays}")