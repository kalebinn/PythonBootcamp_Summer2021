# traditional functions (they look like math)
def f(x):
    return x + 5

def h(x, y):
    return (x ** 2) + (y ** 2)

def j(x, y, z):
    return (x + 1) * (y + 2) * (z - 8)

y = f(1)
print(y)

# functions don't need to have returns 
def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}! Welcome to Canadian Eagle!")


user_first_name = input("Type your first name: ")
user_last_name = input("Type your last name: ")
greet(user_first_name, user_last_name)

