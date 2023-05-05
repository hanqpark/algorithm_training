# 유형: 구현
# 제목: 럭키 스트레이트
# 번호: 18406
# 난도: 브론즈 2
# 일자: 2023년 5월 5일 화요일
# 링크: https://www.acmicpc.net/problem/18406

if __name__ == "__main__":
    n = input()
    front = n[:len(n)//2]
    back = n[len(n)//2:]
    res = "LUCKY" if sum(map(int, front)) == sum(map(int, back)) else "READY"
    print(res)