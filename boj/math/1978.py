primes = [True for _ in range(1001)]
primes[0], primes[1] = False, False
for i in range(2, 1001):
    if primes[i]:
        x = i+i
        while True:
            try:
                primes[x]=False
                x += i
            except IndexError:
                break

int(input())
res = 0
for num in map(int, input().split()):
    if primes[num]: res += 1
print(res)