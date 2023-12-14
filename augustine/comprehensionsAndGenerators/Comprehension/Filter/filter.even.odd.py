# Filter out even and odd numbers from list

tests = [ 0,1,2,3,4,5,6,7,8,9,10]

# result contains odd numbers of the list

result = filter(lambda x : x % 2, tests)
print(list(result))

# result contains even numbers of the list

result = filter(lambda x : x % 2 ==0 , tests)
print(list(result))