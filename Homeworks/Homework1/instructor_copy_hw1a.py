# first, let's get the user input as integer values 
N = int(input('choose a number'))
M = int(input('choose a second number'))

# now we have to use if/else statements to implement the two conditions: 
# - If it is evenly divisible: print the following statement: “[N] is evenly divisible by [M]” 
# - Otherwise: print the following statement: “[N] is not divisible by [M]"
if N % M  == 0:
    print(f'{N} is evenly divisible by {M}')
else:
    print(f'{N} is not evenly divisible by {M}')