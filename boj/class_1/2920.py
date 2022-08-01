lst = list(map(int, input().split()))
asc = [i+1 for i in range(8)]
print(lst, asc)
if lst == asc: print("ascending")
elif lst == sorted(asc, reverse=True): print("descending")
else: print("mixed")