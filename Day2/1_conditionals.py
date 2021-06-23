my_true_bool = True 
my_false_bool = False 

x = 10 
y = 13 

# is x equal to y? 
print(x == y)

# is x greater than y? 
print(x > y)

# is x greater than or equal to y? 
print(x >= y)

# is x less than y? 
print(x < y)

# is x less than or equal to y? 
print(x <= y)

# general structure 
# if/else statement 
if x == y:
    z = x - y
else:
    z = x + y 

print(z)

# conditional statements
# if/else if/else statements
x = 10 
y = 10
if x > y: 
    z = 'x is greater than y.'
elif x == y:
    z = 'x is equal to y.'
else:
    z = 'x is less than y.'

print(z)