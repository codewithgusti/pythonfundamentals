# Return a new list with the string “your name is” + name ,but only if length of name is bigger than 4

names = ['augustine', 'syre', ' dianna', 'akira']

new = list (map(lambda name :f'my name is {name}', filter(lambda x : len(x)> 4, names) ))
print(new)