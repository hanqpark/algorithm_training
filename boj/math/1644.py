n = int(input())
primes = [True for _ in range(n+1)]
primes[0], primes[1] = False, False
for i in range(2, n+1):
    if primes[i]:
        x = i+i
        while 1:
            try:
                primes[x] = False
                x += i
            except IndexError: break
res = 0
prime_nums = list(i for i in range(n+1) if primes[i])
for i in range(len(prime_nums)):
    numsum = prime_nums[i]
    for j in range(i+1, len(prime_nums)):
        numsum += prime_nums[j]
        if numsum >= n: break
    if numsum == n:
        res += 1
print(res)