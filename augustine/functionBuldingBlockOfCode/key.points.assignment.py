# Assignment to parameter names

x = 3
def func(x):
    x=7 # defining local a x , not changing the global one
   
func(x)
print(x)