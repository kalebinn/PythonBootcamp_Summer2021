subtotal = float(input("How much did your food cost? "))
tip_percentage = float(input("What percent do you want to tip (%)? "))
sales_tax = 0.08875

# total = subtotal + (tip_percentage * subtotal) + (sales_tax * subtotal) 
total = round(subtotal + (tip_percentage/100 * subtotal) + (sales_tax * subtotal), 2)
tip_amount = round((tip_percentage/100 * subtotal), 2)
tax_amount = round((sales_tax * subtotal), 2)

print(f'Your subtotal is: ${subtotal}')
print(f'Your tip amount is: ${tip_amount}')
print(f'Your tax amount is: ${tax_amount}')
print(f'Your total is: ${total}')