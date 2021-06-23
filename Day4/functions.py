# f(x) = x + 1
# # if x = 2, f(x) = 3

def f(x):
    return x + 1

# x = 2 
# y = f(x)
# print(y)

# f(x, y) = (x + 2) + (y - 10)
def f(x, y):
    return (x + 2) + (y - 10)

f(4, 5)
f(10, 12)


# f(x, y, z) = z*((x + 2) + (y - 10))
def f(x, y, z):
    return z*((x + 2) + (y - 10))


def greet(first_name, last_name):
    full_name = first_name + " " + last_name
    print(f"Hello {full_name.title()}")

def group_greeting(names):
    for name in names:
        print(f"Hello {name.title()}")

# greet("spongebob", "squarepants")
# greet("patrick", "StAR")

krusty_krab_employees = ["spongebob squarepants", "patrick star", "mr. krabs", "plankton", "squidward"]
students = ["george", "sarah","patrick", "bob", "cindy", "john"]
group_greeting(krusty_krab_employees)
print("-" * 10)
group_greeting(students)