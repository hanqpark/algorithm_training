# 유형: 2차원 배열
# 제목: 색종이
# 번호: 2563
# 난도: 실버 5
# 일자: 2023년 5월 2일 화요일
# 링크: https://www.acmicpc.net/problem/2563


if __name__ == "__main__":
    paper = [[0 for _ in range(101)] for _ in range(101)]
    cnt = 0
    for i in range(int(input())):
        x, y = map(int, input().split())
        for xi in range(x, x+10):
            if xi > 100: break
            for yi in range(y, y+10):
                if yi > 100: break
                if not paper[xi][yi]:
                    paper[xi][yi] = 1
                    cnt += 1
    print(cnt)