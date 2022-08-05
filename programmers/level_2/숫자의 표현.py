def solution(n):
    cnt = 1
    for i in range(1, n):
        s = i
        for j in range(i+1, n):
            if s+j > n : 
                break
            elif s+j == n:
                cnt += 1
                break
            else:
                s += j
    return cnt