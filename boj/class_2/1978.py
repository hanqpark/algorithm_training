def isprime(n):
    if n==1: return 0
    for i in range(2, int(n**0.5)+1):
        if not n%i: return 0
    return 1

n = input()
nums = list(map(int, input().split()))
print(sum(isprime(n) for n in nums))