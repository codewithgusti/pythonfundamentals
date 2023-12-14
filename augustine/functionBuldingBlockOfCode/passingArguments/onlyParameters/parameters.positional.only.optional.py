#“Positional-only parameters can also be optional:”


def func( a, b=2,/):
    print(a,b)
    
func(4,5)
func(3)