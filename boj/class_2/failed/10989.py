import sys, heapq
read = sys.stdin.readline

def solution():
    n = int(sys.stdin.readline())
    num_list = [0] * 10001
    for _ in range(n):
        num_list[int(sys.stdin.readline())] += 1

    for i in range(10001):
        if num_list[i] != 0:
            for j in range(num_list[i]):
                print(i)

def third():
    heap = []
    for _ in range(int(read())):
        heapq.heappush(heap, int(read()))
    while heap:
        print(heapq.heappop(heap))

def second():
    heap = heapq.heapify([int(input()) for _ in range(int(input()))])
    while heap:
        print(heapq.heappop(heap))

def first():
    for i in sorted(int(input()) for _ in range(int(input()))):
        print(i)