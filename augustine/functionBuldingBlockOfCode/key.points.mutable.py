# Changing Mutable object affects the caller

x = [1,2,3]

def func(x):
    # set the second element to 42
    x[1]=42
func(x)
print(x)