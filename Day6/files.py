import random 

AMD_theatre_menu = {
    "Recliner Seating Ticket": 9.99,
    "Regular Seating Ticket" : 4.99, 
    "Small popcorn" : 4.99,
    "Large popcorn" : 7.99,
    "Small Soft Drink" : 1.99,
    "Large Soft Drink" : 3.99
}

menu_options = '''
Tickets Pricing 
-----------------------------
1 - Recliner Seats: 9.99
2 - Regular Seats: 4.99

Food
-----------------------------
3 - Small Popcorn: 4.99
4 - Large popcorn: 7.99
5 - Small Soft Drink: 1.99
6 - Large Soft Drink: 3.99

7 - Finish order

'''
print(menu_options)

user_selection = input("Please make a selection from the menu: ")
subtotal = 0
orders = []

while True:
    if user_selection == '1':
        subtotal = subtotal + AMD_theatre_menu["Recliner Seating Ticket"]
        orders.append("Recliner Seating Ticket")
    elif user_selection == '2':
        subtotal = subtotal + AMD_theatre_menu["Regular Seating Ticket"]
        orders.append("Regular Seating Ticket")
    elif user_selection == '3':
        subtotal = subtotal + AMD_theatre_menu["Small popcorn"]
        orders.append("Small popcorn")
    elif user_selection == '4':
        subtotal = subtotal + AMD_theatre_menu["Large popcorn"]
        orders.append("Large popcorn")
    elif user_selection == '5':
        subtotal = subtotal + AMD_theatre_menu["Small Soft Drink"]
        orders.append("Small Soft Drink")
    elif user_selection == '6':
        subtotal = subtotal + AMD_theatre_menu["Large Soft Drink"]
        orders.append("Large Soft Drink")
    elif user_selection == '7':
        break
    else:
        print("Invalid selection")
    
    user_selection = input("Please make a selection from the menu: ")

print(f"Your subtotal is: ${round(subtotal, 2)}")
ny_tax = 0.08875
final_total = subtotal + (ny_tax * subtotal)
print(f"NY sales tax: {round(ny_tax * subtotal, 2)}")
print(f"Your total is: ${round(final_total, 2)}")

print("Please wait, your tickets and receipts are printing!")

# printing the receipt 
invoice_number = random.randint(10000, 99999)

my_file = open(f"AMD_receipt_{invoice_number}.txt", "w")
my_file.write("Hello! Welcome to AMD Theatres!\n\n")
my_file.write(f"Invoice #{invoice_number}\n\n")

my_file.write("------------------------------------\n")
for order in set(orders): 
    num_times_ordered = orders.count(order)
    my_file.write(f"{num_times_ordered} x {order}: ${num_times_ordered * AMD_theatre_menu[order]}\n")

my_file.write(f"\nSubtotal: ${round(subtotal, 2)}\n")
my_file.write(f"NY Sales Tax: {round(ny_tax * subtotal, 2)}\n")
my_file.write("------------------------------------\n")
my_file.write(f"Total: ${round(final_total, 2)}\n\n\n")

refund_policy = '''
Refund Policy: 
Return the ticket within 24 hour of 
showtime to receive a full refund. No 
refunds will be given for cancellations 
less than 24 hours before the start time 
of the requested movie.
'''
my_file.write(refund_policy)

print(orders.count("Recliner Seating Ticket"))






