from sys import stdin

stack = []
read = stdin.readline
for _ in range(int(read())):
    s = read().split()
    if "pop" == s[0]:
        res = -1 if not stack else stack.pop()
        print(res)
    elif "size" == s[0]:
        print(len(stack))
    elif "empty" == s[0]:
        res = 0 if stack else 1
        print(res)
    elif "top" == s[0]:
        res = -1 if not stack else stack[-1]
        print(res)
    else:
        stack.append(s[-1])
    