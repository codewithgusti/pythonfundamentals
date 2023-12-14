
def outer():
    test = 1 # outer scope
    def inner():
        global test  # nearest enclosing scope (which is the outer scope)
        test = 2
        print('inner :', test)
    inner()
    print('outer :' , test)
test = 0 # global scope
outer()
print('global :', test)