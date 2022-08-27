# 220827
# BOJ 18870번 좌표 압축
# 난이도: 실버 2
# https://www.acmicpc.net/problem/18870
# 문제 풀이 핵심: list.index(x)는 역시 시간이 오래 걸린다.

n = int(input())
xs = list(map(int, input().split()))
dic = {x: i for i, x in enumerate(sorted(set(xs)))}
res = [dic[x] for x in xs]
print(*res)