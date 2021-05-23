''' 빠른 A+B '''
import sys
read = sys.stdin.readline

for _ in range(int(read())):
    a, b = read().split()
    print(int(a)+int(b))