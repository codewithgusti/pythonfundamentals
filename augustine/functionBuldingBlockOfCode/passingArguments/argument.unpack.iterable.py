# Iterable unpacking
# Iterable unpacking uses the syntax *iterable_name to pass the elements of an iterable as positional arguments to a function:
    

def func(a,b,c):
    print(a,b,c)
values = (1,2,-7)
func(*values)