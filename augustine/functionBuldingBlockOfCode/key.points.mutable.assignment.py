# Assigning an object to an parameter name within a function doesn't affect the caller.

x = [1,2,3]

def func(x):
    # set the second element to 42
    x[1]=42
    # this points to a new string object
    x = 'Something else'
func(x)
print(x)
