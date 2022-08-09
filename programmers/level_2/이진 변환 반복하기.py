def solution(s):
    cnt, zero_cnt = 0, 0
    while len(s) > 1:
        cnt += 1
        zero_cnt += s.count("0")
        s = bin(s.count("1"))[2:]
    return [cnt, zero_cnt]
    
        