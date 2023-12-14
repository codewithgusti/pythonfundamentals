#“Python provides you with the ability to do this by using variable positional parameters. 
# Let's look at a very common use case, the minimum() function.
# This is a function that calculates the minimum of its input values:”

def minimum(*n):
    #print(type(n))
    if n:
        mn = n[0]
        for value in n[1:]:
           if value < mn:
                mn =value
        print(mn)

minimum(1,3,-7,9)
