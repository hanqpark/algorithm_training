# 유형: 일반 수학
# 제목: 중앙 이동 알고리즘
# 번호: 2903
# 난도: 브론즈 3
# 일자: 2023년 5월 2일 화요일
# 링크: https://www.acmicpc.net/problem/2903


if __name__ == "__main__":
    a = 2
    for i in range(int(input())):
        a += a-1
    print(a*a)