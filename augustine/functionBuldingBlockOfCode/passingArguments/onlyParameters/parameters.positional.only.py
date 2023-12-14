# Positional Only Parameters

def func(a,b,/,c):
    print(a,b,c)

func(1,2,c=3)
#func() got some positional-only arguments passed as keyword arguments
#func(1,b=2,c=5)