from collections import deque

def solution(s):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    words3 = ["zer", "one", "two", "thr", "fou", "fiv", "six", "sev", "eig", "nin"]
    string = deque(s)
    answer = ""
    while string:
        c = string.popleft()
        if c.isdigit():                     # isdigit(c)가 아니라 c.isdigit()임!!
            answer += c
        else:
            c2 = string.popleft()
            c3 = string.popleft()
            temp = c+c2+c3
            idx = words3.index(temp)        # list에서는 find가 아닌 index 사용!!
            answer += str(idx)
            for _ in range(len(words[idx])-3):
                string.popleft()
    return int(answer)
            
            