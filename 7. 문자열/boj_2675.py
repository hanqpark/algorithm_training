'''문자열 반복'''
import sys
read = sys.stdin.readline

for _ in range(int(read())):
    n, s = map(str, read().split())
    string = ''
    for ss in s:
        string += ss*int(n)
    print(string)