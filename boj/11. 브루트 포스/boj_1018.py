import sys
read = sys.stdin.readline

n, m = map(int, read().split())
chess = []
for _ in range(n):
    chess.append(list(read()))

char, min_val = 'W', n*m
for i in range(n-7):
    for j in range(m-7):
        true, false = 0, 0
        for x in range(8):
            char = 'W' if char == 'B' else 'B'
            for y in range(8):
                char = 'W' if char == 'B' else 'B'
                if chess[i+x][j+y] == char: true += 1
                else: false += 1
        temp = min(true, false)
        min_val = temp if temp < min_val else min_val
print(min_val)