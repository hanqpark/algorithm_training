def solution(n):
    ans = 1
    while n > 1:
        if n%2:
            ans += 1
            n-=1
        else:
            n//=2
    return ans

def binary(n):
    return bin(n).count('1')