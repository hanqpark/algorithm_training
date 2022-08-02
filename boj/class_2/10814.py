import sys

read = sys.stdin.readline
for person in sorted(read() for _ in range(int(read()))):
    print(person)

