# ternary.py

order_amount = input('Enter your order amount : ')
order_total = int(order_amount)

# classical if/else
'''
if order_total > 100:
    discount = 25
else:
    discount = 0
print(order_total,discount)
'''

# ternary operator

discount = 25 if order_total > 100 else 0
print(f'the order_total is ${order_total} with {discount} discount')