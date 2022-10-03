# 221003
# 프로그래머스 11729번 하노이 탑 이동 순서
# 분류: 재귀
# 난이도: 실버 1
# https://www.acmicpc.net/problem/11729
# 한줄 평: https://sikaleo.tistory.com/29 -> 하노이의 탑도 어떻게 하는지 다 까먹었다 ㅎㅎ

def hanoi(n, a, c, b):
    global cnt, proc
    if n == 1:
        cnt += 1
        proc.append([a, c])
        return
    hanoi(n-1, a, b, c)
    cnt += 1; proc.append([a, c])
    hanoi(n-1, b, c, a)

if __name__ == "__main__":
    cnt, proc = 0, []
    hanoi(int(input()), 1, 3, 2)
    print(cnt)
    for p in proc: print(*p)
