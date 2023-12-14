# primes

primes = []

upto = 100

for n in range(2, upto + 1):
    _isPrime = True # flag
    for divisor in range(2,n):
        if n % divisor ==0:
            _isPrime = False
            break
    if _isPrime:
        primes.append(n)
print(primes)
