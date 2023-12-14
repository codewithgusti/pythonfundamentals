from functools import reduce

# Find Multiply of all elements in list

tests =[1,2,3,4,5,6]

multiply = reduce(lambda a , b : a*b, tests)
print(f'All elements in sequence are over so it returns {multiply} ')