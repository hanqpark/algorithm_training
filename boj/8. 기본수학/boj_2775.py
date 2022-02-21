for _ in range(int(input())):
    k = int(input())
    n = int(input())
    apart = [[i+1 for i in range(n)]]
    for i in range(k):
        temp = []
        for j in range(n):
            temp.append(sum(apart[i][:j+1]))
        apart.append(temp)
    print(apart[-1][-1])