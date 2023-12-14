# Local vs Global

# we define a function, called local”
def local():
    m=7
    print(m)

# we define m within the global
m=5

local()
print(m) 