def sales_total_calculator(subtotal, tax, tip):
    sales_total = subtotal + (subtotal * tax) + (subtotal * tip)
    return round(sales_total, 2)

ny_tax = 0.08875

tip_percentage = float(input("How much would you like to tip (%)? "))
tip_percentage = tip_percentage / 100

subtotal = float(input("What is your subtotal? $"))

final_total = sales_total_calculator(subtotal, ny_tax, tip_percentage)
print(f"Your total is: ${final_total}")