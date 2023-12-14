# “Python 3 introduced keyword-only parameters. 
# We are going to study them only briefly, as their use cases are not that frequent.
# There are two ways of specifying them, either after the variable positional parameters, or after a bare *.
# Let's see an example of both:”

def kwo(*a,c):
    print(a,c)
kwo(1,2,3 , c= 7)
kwo(c=4)
#kwo() missing 1 required keyword-only argument: 'c'
#kwo(1,3)