''' X보다 작은 수 '''
import sys
read = sys.stdin.readline

n, x = map(int, read().split())
a = list(map(int, read().split()))

for i in a:
    if i < x:
        print(i, end=" ")