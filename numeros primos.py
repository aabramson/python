limit = 17000
numbers = [_ for _ in range (2, limit + 1) ]
primes = []

while numbers:
    candidate = numbers [0]
    primes.append (candidate)
    factor = 1
    product = factor * candidate
    while product <= limit:
        if product in numbers: numbers.remove (product)
        factor += 1
        product = factor * candidate

print (primes)