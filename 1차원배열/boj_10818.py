'''최소, 최대'''

import sys
read = sys.stdin.readline

n = int(read())
a = list(map(int, read().split()))
print(min(a), max(a))