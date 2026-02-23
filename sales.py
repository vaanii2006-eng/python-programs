# Prices of products
laptop_price = 50000
mobile_price = 20000
headphone_price = 2000

# Taking quantity from user
laptop_qty = int(input("Enter number of Laptops: "))
mobile_qty = int(input("Enter number of Mobiles: "))
headphone_qty = int(input("Enter number of Headphones: "))

# Calculate total amount
total = (laptop_price * laptop_qty) + \
        (mobile_price * mobile_qty) + \
        (headphone_price * headphone_qty)

print("Total Amount:", total)

# Apply discount
if total > 50000:
    discount = total * 0.10
elif total > 20000:
    discount = total * 0.05
else:
    discount = 0

final_amount = total - discount

print("Discount:", discount)
print("Final Amount to Pay:", final_amount)
