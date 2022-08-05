def solution(n):
    cond = bin(n).count("1")
    while True:
        if cond == bin(n+1).count("1"): return n+1
        n += 1