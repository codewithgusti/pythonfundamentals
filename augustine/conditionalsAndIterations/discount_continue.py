#Let's say you want to apply a 20% discount to all products in a basket list
# for those that have an expiration date of today. 
# The way you achieve this is to use the continue statement,
# which tells the looping construct (for or while) to stop execution of the body immediately
# and go to the next iteration, if any.
# This example will take us a little deeper down the rabbit hole,
# so be ready to jump:”

from datetime import date,timedelta
today = date.today()
tomorrow = today + timedelta(days=1) 

products =[
    {"fruit":"apple", "price":20,"expiry_date": today},
    {"fruit":"banana", "price":100,"expiry_date": tomorrow}, 
    {"fruit":"orange", "price":150,"expiry_date": today},
]

for product in products:
    if product["expiry_date"] != today:
        continue
    product['price'] *= 0.8
    print('price of fruit',product['fruit'],'is now : R',product['price'])
    