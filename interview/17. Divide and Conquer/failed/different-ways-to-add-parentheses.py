# https://leetcode.com/problems/different-ways-to-add-parentheses/

def compute(left, right, op):
    res = []
    for l in left:
        for r in right:
            res.append(eval(str(l) + op + str(r)))
    return res

def sol(expression):   
    if expression.isdigit():
        return [int(expression)]
    
    res = []
    for i, v in enumerate(expression):
        if v in "+-*":
            l = sol(expression[:i])
            r = sol(expression[i+1:])                
            res.extend(compute(l,r,v))
    return res


if __name__ == "__main__":
    expression = "2*3-4*5"
    res = sol(expression)
    print(res)