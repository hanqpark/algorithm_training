import sys
read = sys.stdin.readline

stack = []
for _ in range(int(read())):
    n = int(read())
    if n:
        stack.append(n)
    else:
        if stack:
            stack.pop()
print(sum(stack))