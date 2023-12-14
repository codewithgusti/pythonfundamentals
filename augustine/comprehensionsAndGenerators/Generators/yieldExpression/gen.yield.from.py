def print_squares(start, end):
    yield from (n ** 2 for n in range(start, end))


for element in print_squares(2, 5):
    print(element)
