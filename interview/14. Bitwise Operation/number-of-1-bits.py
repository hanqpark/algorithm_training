def hammingWeight(n):
    return bin(n).count("1")

def solution(n):
    cnt = 0
    while n:
        n &= n-1
        cnt += 1
    return cnt

if __name__ == "__main__":
    res = solution(11)
    print(res)