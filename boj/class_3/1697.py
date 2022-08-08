n, k = map(int, input().split())
print(bin(abs(n-k)).count('1'))