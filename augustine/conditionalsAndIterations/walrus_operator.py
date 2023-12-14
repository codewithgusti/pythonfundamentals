# using Walrus Operator

remainder = value % modulus

if remainder:
    print(f'Not divisible ! , The remainder {remainder}. ')
    
# With assignment expression 

if remainder :=value % modulus:
    print(f'Not divisible ! , The remainder {remainder}. ')