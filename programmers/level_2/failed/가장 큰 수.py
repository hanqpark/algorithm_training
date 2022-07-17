def solution(numbers):
    numbers = list(map(str, numbers))
    # lambda 값이 numbers에 저장되는 것이 아닌 그냥 비교를 위해서 값을 부풀려주는 것일 뿐......
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))