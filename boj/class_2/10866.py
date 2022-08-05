from collections import deque
from sys import stdin

read = stdin.readline
dq = deque()

for _ in range(int(read())):
    s = read().split()
    if "push_front" == s[0]:
        dq.appendleft(s[-1])
    elif "push_back" == s[0]:
        dq.append(s[-1])
    elif "pop_front" == s[0]:
        res = -1 if not dq else dq.popleft()
        print(res)
    elif "pop_back" == s[0]:
        res = -1 if not dq else dq.pop()
        print(res)
    elif "size" == s[0]:
        print(len(dq))
    elif "empty" == s[0]:
        res = 0 if dq else 1
        print(res)
    elif "front" == s[0]:
        res = -1 if not dq else dq[0]
        print(res)
    elif "back" == s[0]:
        res = -1 if not dq else dq[-1]
        print(res)