import sys, copy
read = sys.stdin.readline

def main(today, round=1):
    tomorrow = copy.deepcopy(today)
    for b in range(n):
        for a in range(m):
            if today[b][a] == 1:
                for dx, dy in zip(xs, ys):
                        x, y = dx+a, dy+b
                        if -1<x<m and -1<y<n and today[y][x]==0:
                            tomorrow[y][x] = 1
                            changed = True
        if changed:
            today = tomorrow
            round += 1
        else:
            real = m*n-sum(tomorrow, []).count(-1)
            return round-1 if real == expect else -1

if __name__ == "__main__":
    xs, ys = [1, 0, -1, 0], [0, 1, 0, -1]
    m, n = map(int, read().split())
    today = [list(map(int, read().split())) for _ in range(n)]
    expect = m*n-sum(today, []).count(-1)
    print(main(today))