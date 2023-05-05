# 유형: 2차원 배열
# 제목: 세로읽기
# 번호: 10798
# 난도: 브론즈 1
# 일자: 2023년 5월 2일 화요일
# 링크: https://www.acmicpc.net/problem/10798


if __name__ == "__main__":
    strs = list(input() for _ in range(5))
    ans = ""
    for i in range(15):
        for s in strs:
            if i < len(s):
                ans += s[i]
    print(ans)