# Find the square of all elements in the list

# iterables
nums = [ 1, 2 , 3, 4 , 5, 6, 7]
# function
def find_square(number):
    return number *number

square = list (map(find_square, nums))
print(square)


