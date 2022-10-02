money = int(input())
res = 0
for _ in range(int(input())):
    don, cnt = map(int, input().split())
    res += don*cnt
ans = "Yes" if res==money else "No"
print(ans)