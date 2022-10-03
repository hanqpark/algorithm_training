def eratos(n, k):
    primes = [True for _ in range(n+1)]
    for i in range(2, n+1):
        if primes[i]:
            x = i
            while True:
                try:
                    if primes[x]:
                        k -= 1
                        primes[x] = False
                    if not k: return x
                    x += i
                except IndexError:
                    break
    
n, k = map(int, input().split())
print(eratos(n, k))