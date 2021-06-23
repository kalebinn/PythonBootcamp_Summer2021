import random 

# “Orange” “Seven” “Jackpot” “Apple” “Cherry” “Bar” “Dollar” “Ace”
possibilities = ["Orange", "Seven", "Jackpot", "Apple", "Cherry", "Bar", "Dollar", "Ace"] 
number_of_strips = 3 


number_of_plays = 0
number_of_games = 1000000000000
number_of_simulations = 10000
simulation_results = []
# user_selection = input("Press 1 to play, press anything else to exit.\n")

for simulation in range(0, number_of_simulations):
    for play in range(0, number_of_games):
        number_of_plays = number_of_plays + 1
        user_won = True
        outcomes = random.choices(possibilities, k=number_of_strips)
        # print(outcomes)

        for strip in outcomes:
            if strip != 'Jackpot':
                user_won = False

        if user_won == True:
            # print("JACKPOT YOU WIN!!!")
            break
        else:
            # print("Sorry, better luck next time.")
            pass 
    
    simulation_results.append(number_of_plays)
    number_of_plays = 0

        # user_selection = input("Press 1 to play again, press anything else to exit.\n")    

print('good bye')

for result in simulation_results:
    print(f"Played: {result} times before winning.")
    cost_per_play = 5
    print(f"Money spent: $ {cost_per_play * result}")

average_times_played = sum(simulation_results)/len(simulation_results)
print(f"Average times plays: {average_times_played}")
print(f"Average money spent: {average_times_played * cost_per_play}")

# probability_of_winning = times_won/number_of_games
# number_of_possibilities = len(possibilities) #in this case, it is 8
# calculated_prob = 1/(number_of_possibilities ** number_of_strips)

# print(f"Number of wins = {times_won}")
# print(f"(Monte Carlo) Probability of winning = {probability_of_winning}")
# print(f"Calculated Probability of winning = {calculated_prob}")