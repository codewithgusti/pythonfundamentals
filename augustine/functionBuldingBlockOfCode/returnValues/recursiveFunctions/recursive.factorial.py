
def factorial(n):
    if n in (0, 1):
        return 1    # Base Case
    return factorial(n-1)* n

print(factorial(5))