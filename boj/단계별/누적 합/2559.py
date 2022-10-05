# 221005
# 프로그래머스 2559 수열
# 분류: 누적 합
# 난이도: 실버 3
# https://www.acmicpc.net/problem/2559
# 한줄 평: 다 푼건데.. 실수해서 망해버렸다 ㅠㅠ / 반례: 3 1 / -1 -2 -3 -> -2 출력됏음

n, k = map(int, input().split())
temps = list(map(int, input().split()))

if n==k:
    print(sum(temps))
else:
    cumsum = sum(temps[:k])
    maxi = cumsum
    for i in range(n-k):
        tmp = cumsum-temps[i]+temps[i+k]
        maxi = max(maxi, tmp)
        cumsum = tmp
    print(maxi)