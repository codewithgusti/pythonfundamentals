

def print_sqaures(start , end):
    for n in range(start,end):
        yield n ** 2

for n in print_sqaures(2,5):
    print(n)