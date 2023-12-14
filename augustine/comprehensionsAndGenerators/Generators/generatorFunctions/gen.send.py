# When we call generator.send(), the value that we feed to send will be passed into the generator,
# execution is resumed, and we can fetch it via the yield expression.
# This is all very complicated when explained with words,
# so let's see an example:

def counter(start=0):
    n = start
    while True:
        result = yield n
        print(type(result), result)
        if result == 'Q':
            break
        n += 1

c = counter()
print(next(c))
print(c.send('wow !!'))
print(next(c))
print(c.send('Q'))
