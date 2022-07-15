def solution(sizes):
    x, y = 0, 0
    for size in sizes:
        size.sort(reverse=True)
        x, y = max(x, size[0]), max(y, size[1])
    return x*y