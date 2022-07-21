def solution(s):
    ans = []
    for c in s:
        if c == "(":
            ans.append(c)
        else:
            if "(" in ans:
                ans.pop()
            else:
                return False
    return False if ans else True