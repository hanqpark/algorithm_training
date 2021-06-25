'''상수'''
n1, n2 = input().split()
new_n1 = "".join(reversed(list(n1)))
new_n2 = "".join(reversed(list(n2)))
print(new_n1 if new_n1 > new_n2 else new_n2)