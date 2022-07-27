# https://leetcode.com/problems/sum-of-two-integers

def solution(a, b):
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF
    
    while b!=0:
        a, b = (a^b)&MASK, ((a&b)<<1)&MASK
        
    if a > INT_MAX:
        a = ~(a^MASK)
    return a


res = solution(14345, 4124)
print(res)