
def get_multiple_of_five(n):
    return list(filter(lambda k : not k % 5, range(n)))
print(get_multiple_of_five(100))