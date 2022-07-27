from math import gcd

def GCD(maxl, minl):
    if minl == 0:
        return maxl
    else:
        return GCD(minl, maxl%minl)

def LCM(maxl, minl):
    return maxl*minl//GCD(maxl, minl)
    
def wrong_ans(w,h):
    max_len, min_len = max(w, h), min(w, h)
    g = GCD(max_len, min_len)
    length = max_len/min_len
    new_length = length
    cnt = 0
    for i in range(1, int(max_len/g)+1):
        if i < new_length:
            cnt += 1
        elif i > new_length:
            cnt += 2
            new_length += length
        elif i == new_length:
            cnt += 1
            new_length += length
        print(f"순서: {i}, count: {cnt}, length: {new_length}")
    return w*h-cnt*max_len/int(max_len/g)


def solution(w,h):
    return w*h-w-h+gcd(w,h)


if __name__ == "__main__":
    g = GCD(6, 4)
    l = LCM(6, 4)
    print(g)
    print(l)