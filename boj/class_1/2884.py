h, m = map(int, input().split())
if m < 45:
    m += 15
    h = h-1 if h else 23
else:
    m = m-45
print(h, m)