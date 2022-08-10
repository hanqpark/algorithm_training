fib = [0,1,1,2,3,5]

def solution(n):
    if n < 6:
        return fib[n]
    else:
        for i in range(6, n+1):
            tmp = (fib[i-1]+fib[i-2])%1234567
            fib.append(tmp)
        return fib[n]