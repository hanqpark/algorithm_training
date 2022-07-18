import itertools, math

def is_prime(num):
    if num==0 or num==1:
        return False
    
    # 소수 판별할 때 제곱근을 사용하면 빠르대서 사용함
    # test case 2, 10, 11이 오류가 떠서 그냥 2로 나눠 줬음... 
    # 어차피 숫자가 크지 않아서 ㄱㅊ은듯
    for i in range(2, num//2+1):    
        if num % i == 0:
            return False
    return True


def solution(numbers):
    length, answer = len(numbers), []
    for i in range(1, length+1):
        cases = set(itertools.permutations(numbers, i))
        for case in cases:
            num = int("".join(case))
            if is_prime(num):
                answer.append(num)
    print(set(answer))
    return len(set(answer))