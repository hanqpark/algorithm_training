# https://leetcode.com/problems/daily-temperatures/

temp = [73,74,75,71,69,72,76,73]
stack, ans = [], [0 for _ in range(len(temp))]
for i, t in enumerate(temp):
    while stack and t > temp[stack[-1]]:
        last = stack.pop()
        ans[last] = i - last
    stack.append(i)
print(ans)