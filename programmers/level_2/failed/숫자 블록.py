def solution(begin, end):
    res = []
    for i in range(begin, end+1):
        if i == 1:
            res.append(0)
        else:
            flag = True
            for j in range(2, int(i**0.5)+1):
                if not i%j and i//j < 10000000: 
                    res.append(i//j)
                    flag = False
                    break
            if flag:
                res.append(1)   
    return res