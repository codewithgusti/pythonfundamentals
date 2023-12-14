#“Dictionary unpacking
# Dictionary unpacking is to keyword arguments what iterable unpacking is to positional arguments.
# We use the syntax **dictionary_name to pass keyword arguments, 
# constructed from the keys and values of a dictionary, to a function

def func(a,b,c):
    print(a,b,c)
values = {'b':20,'c':30,'a':10}
func(**values)