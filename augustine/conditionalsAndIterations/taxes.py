#If your income is less than $10,000, you don't need to pay any taxes. 
# If it is between $10,000 and $30,000, you have to pay 20% in taxes.
# If it is between $30,000 and $100,000, you pay 35% in taxes, and 
# if you're fortunate enough to earn over $100,000, you must pay 45% in taxes.


# Let's put this all down into beautiful Python code
try :
    amount = input('Enter your income amount:')

    income = int(amount)

    if income < 10000:
        tax_coefficient = 0.0
    elif income < 30000:
        tax_coefficient = 0.20
    elif income < 100000:
        tax_coefficient = 0.35
    else:
        tax_coefficient = 0.40
    print(f'you will pay : ${income * tax_coefficient} in taxes')
except:
    print("Please enter a number")