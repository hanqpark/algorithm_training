res = [0, 1, 2, 3, 5]

def solution(n):
    if n < 5:
        return res[n]
    else:
        for i in range(5, n+1):
            cnt = res[i-1]+res[i-2]
            res.append(cnt%10007)
        return res[-1]
    
print(solution(int(input())))