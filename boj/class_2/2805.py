def cutting(l, r, trees, m):
    while l <= r:
        mid = (l+r)//2
        cut = sum(t-mid for t in trees if t > mid)
        if cut > m:
            l = mid+1
        elif cut < m:
            r = mid-1
        else:
            return mid
    return r

if __name__ == "__main__":
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))
    l, r = 0, max(trees)
    res = cutting(l, r, trees, m)
    print(res)
