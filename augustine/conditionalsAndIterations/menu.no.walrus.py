#suppose we are writing an interactive script that allows customers at an ice cream shop to choose what flavor they want.
#To avoid confusion when preparing orders,
# we want to ensure that the user chooses one of the available flavors. 
# Without assignment expressions, we might write something like this:”

flavors = ['vanilla','chocolate','strawberry','malaga','pistachio']

prompt = "choose your flavor : "
print(flavors)
while True:
    choice = input(prompt)
    if choice in flavors:
        break
    print(f"Sorry your '{choice}' is not valid a option")
print(f"You chose '{choice}' ")

