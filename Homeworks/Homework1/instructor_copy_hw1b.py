# Write a loop that counts backwards by 7 from 1000

# Solution 1: using a while loop 
num = 1000
ending_num = 0 
while num > ending_num:
    print(num)
    num = num - 7

# Solution 2: using a for loop
for num in range(1000, 0, -7):
    print(num)