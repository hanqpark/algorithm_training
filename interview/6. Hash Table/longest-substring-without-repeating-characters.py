# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def mysol(s):
    max_len = 0
    s.strip()
    for i in range(len(s)):
        substring = [s[i]]
        for j in range(i+1, len(s)):
            if s[j] in substring:
                break
            else:
                substring.append(s[j])
        max_len = max(len(substring), max_len)
    return max_len
    
def sol(s):
    used = {}
    max_len = start = 0
    for idx, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_len = max(max_len, idx-start+1)
        used[c] = idx
    return max_len
    
s = "pwwkew"
print(sol(s))