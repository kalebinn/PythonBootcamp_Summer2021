import random 


possibilities = ['lemon', 'cherry', 'watermelon', 'lime', 'peach', 'JACKPOT', 'apple', 'orange']


maximum_index = len(possibilities) - 1
first_outcome_index = random.randint(0, maximum_index)
second_outcome_index = random.randint(0, maximum_index)
third_outcome_index = random.randint(0, maximum_index)

first_outcome = possibilities[first_outcome_index]
second_outcome = possibilities[second_outcome_index]
third_outcome = possibilities[third_outcome_index]


print("Press 1 to spin the slot machine")
print("Press anything else to walk away")

user_choice = input("Enter your choice: ")

if user_choice == '1':
    print(f"| {first_outcome} | {second_outcome} | {third_outcome} |")
else:
    print("Goodbye.")