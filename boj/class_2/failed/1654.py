from sys import stdin

if __name__ == "__main__":
    read = stdin.readline
    k, n = map(int, read().split())
    lans = [int(read()) for _ in range(k)]
    start, end = 1, max(lans)
    
    while start <= end:
        mid = (start+end) // 2
        lines = sum(l//mid for l in lans)
        if lines >= n:
            start = mid + 1
        else:
            end = mid -1
    print(end)