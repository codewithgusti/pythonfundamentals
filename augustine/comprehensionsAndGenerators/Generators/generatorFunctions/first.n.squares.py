# generators

# classical function
def get_squares(n):
    return [x ** 2 for x in range(n)]

print(get_squares(10))

# generator function
def get_square_gen(n):
    for x in range(n):
        yield x ** 2

squares = get_square_gen(10)

print(list(squares))