import sys
read = sys.stdin.readline

x, y, w, h = map(int, read().split())
print(min(x-0, w-x, y-0, h-y))