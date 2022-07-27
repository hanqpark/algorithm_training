def my_solution(x,y):
    ans = bin(x^y)
    return len([one for one in str(ans)[2:] if one=="1"])

def sol(x,y):
    return bin(x^y).count("1")