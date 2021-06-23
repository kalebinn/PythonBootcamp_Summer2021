import random 

# raffle_tickets = [1106, 825, 6419, 420, 55, 94, 11, 22, 25, 100, 50]
raffle_contestants = ['Kelvin', 'Momodou', 'Abdoulaye', 'Stephanie', 'Theodore', 'Thierno', 'Yassine']

maximum_index = len(raffle_contestants) - 1
winning_index = random.randint(0, maximum_index)
winner = raffle_contestants[winning_index]

print(f"The winner is: {winner}")


