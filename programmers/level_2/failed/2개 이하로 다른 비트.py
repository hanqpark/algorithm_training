def mysol(numbers):
    ans = []
    for num in numbers:
        for i in range(num+1, pow(10,15)+1):
            if bin(i^num).count("1") in (1,2):
                ans.append(i)
                break
    return ans


def solution_2(numbers):
    return [(((num ^ (num+1)) >> 2) +num +1) for num in numbers]

solution_2([7, 15])