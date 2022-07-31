# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import Counter

def solution(s, k):
    l = r = 0
    cnts = Counter()
    for r in range(1, len(s)+1):
        cnts[s[r-1]]+=1
        max_char_n = cnts.most_common(1)[0][1]
        
        if r-l-max_char_n > k:
            cnts[s[l]] -= 1
            l += 1
    return r-l

if __name__ == "__main__":
    s = "AABABBA"
    k = 2
    res = solution(s, k)
    print(res)