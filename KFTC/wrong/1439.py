# 유형: 그리디
# 제목: 뒤집기
# 번호: 1439
# 난도: 실버 5
# 일자: 2023년 5월 5일 금요일
# 링크: https://www.acmicpc.net/problem/1439
# 틀린 이유: 테스트 케이스를 충분히 생각해보지 못함

if __name__ == "__main__":
    num = input()
    before = num[0]
    zero, one = 0, 0
    for i in range(1, len(num)):
        if before != num[i]:
            if before == "0": 
                zero += 1
            else: 
                one += 1
            before = num[i]
            
    if num[0] != num[-1]:
        if num[-1] == "0":
            zero += 1
        else:
            one += 1
            
    print(min(zero, one))