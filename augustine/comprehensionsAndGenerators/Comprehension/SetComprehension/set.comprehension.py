
word = 'Hello'
letters1 = { c for c in word}
print(letters1)
letters2 = set(c for c in word)
print(letters2)

print(letters1 ==letters2)