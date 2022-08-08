# https://velog.io/@falling_star3/파이썬-순열-조합-중복순열-중복조합itertools를-활용한-구현
# 중복순열 -> product(list, repeat=i)
# 중복조합 -> combinations_with_replacement(list, i)

from itertools import product

def solution(word):
    mother = ["A", "E", "I", "O", "U"]
    words = []
    for i in range(1, 6):
        for w in product(mother, repeat=i):
            words.append("".join(w))
    words.sort()
    return words.index(word)+1