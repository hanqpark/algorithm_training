# 나의 풀이
# 시간복잡도에서 탈락
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        front = phone_book[i]
        for j in range(i+1, len(phone_book)):
            back = phone_book[j]
            if back.startswith(front):
                return False
    return True


# zip을 효율적으로 활용하는 방법
# 나의 풀이랑 아이디어 제일 비슷함 -> zip을 잘 활용해보자!
def solution(phoneBook):
    phoneBook.sort()
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


# heap을 활용하는 방법
import heapq
def solution(pb):
    heapq.heapify(pb)
    # print(type(pb))
    p = heapq.heappop(pb)
    while pb :
        if pb[0].startswith(p) : return False
        p = heapq.heappop(pb)
    return True


# hashmap을 활용하는 방법
def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True


# 조합을 사용하여 빠르게 iteration하는 방법
# 시간복잡도에서 탈락
from itertools import combinations
def solution(phoneBook):
    sortedPB = sorted(phoneBook, key= len)
    for (a,b) in combinations(sortedPB, 2):
        if b.startswith(a): return False
    return True

