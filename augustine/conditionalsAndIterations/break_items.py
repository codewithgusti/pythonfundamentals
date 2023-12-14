#“Say we want to tell whether at least one of the elements in a list evaluates to True
# when fed to the bool() function. Given that we need to know whether there is at least one,
# when we find it, we don't need to keep scanning the list any further. 
# In Python code, this translates to using the break statement. 
# Let's write this down into code:

items = [0,None,0.0, True,0,7]
found = False # this a flag

for item in items:
    print('Scanning items',item)
    if item:
        found = True # update the flag
        break
if found:
    print('At least one item evaluates to True')
else:
    print('All items evaluates to False')

