# 유형: 일반 수학
# 제목: 분수찾기
# 번호: 1193
# 난도: 실버 5
# 일자: 2023년 5월 2일 화요일
# 링크: https://www.acmicpc.net/problem/1193


n = int(input())
start = 1
for i in range(1, 10000000):
    start += i
    if start >= n:
        break
        
diff = start-n
ans = f"{1+diff}/{i-diff}" if diff else f"{1+diff}/{i-diff+1}"
print(ans)
    