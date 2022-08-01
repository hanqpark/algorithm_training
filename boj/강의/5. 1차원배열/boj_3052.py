'''나머지'''

a = []
for _ in range(10):
    n = int(input()) % 42
    if n not in a:
        a.append(n)
print(len(a))
