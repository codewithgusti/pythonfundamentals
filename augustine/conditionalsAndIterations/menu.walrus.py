# using walrus operator

flavors = [
    'vanilla',
    'chocolate',
    'strawberry',
    'malaga',
    'pistachio'
    ]

prompt = "choose your flavor : "
print(flavors)

while (choice := input(prompt)) not in flavors:
    print(f"Sorry your '{choice}' is not valid a option")
print(f"You chose '{choice}' ")