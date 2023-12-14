# generator function
def get_square_gen(n):
    for x in range(n):
        yield x ** 2


squares = get_square_gen(10)

print(squares.__next__())