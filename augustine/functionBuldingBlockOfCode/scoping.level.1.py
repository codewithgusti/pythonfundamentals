# Scope and name resolution

def my_function():
    #test = 1 # This is defined in the local scope of my_function
    print('local : ',test)

test = 0 # This is defined defined in the global scope of the function
my_function()
print('global : ', test)