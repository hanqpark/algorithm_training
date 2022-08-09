zero = [1, 0, 1, 1, 2, 3]
one = [0, 1, 1, 2, 3, 5]
for i in range(6, 41):
    zero.append(zero[i-1]+zero[i-2])
    one.append(one[i-1]+one[i-2])

for _ in range(int(input())):
    n = int(input())
    print(zero[n], one[n])