#“Variable keyword parameters are very similar to variable positional parameters. 
# The only difference is the syntax (** instead of *)
# and the fact that they are collected in a dictionary:”

def func(**kwargs):
    print(kwargs)

func()
func(a=1,b=42)
func(a=1,b=46,c=92)