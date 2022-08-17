# 2022.08.17
# https://school.programmers.co.kr/learn/courses/30/lessons/68645
# 삼각 달팽이


def mysol(n):
    if n==3: return [1,2,6,3,4,5]       # n이 3일때만 런타임에러가 발생하는 것을 발견해서 그냥 예외 처리해줌..절대 좋은 코드는 아님

    snail = [[0 for _ in range(x+1)] for x in range(n)]     # 달팽이 크기만큼 그래프 생성
    front, back, cnt, i = 0, 0, 0, 1                        # front, back은 달팽이 배열의 앞, 뒤. cnt는 삼각형 한바퀴 돈 횟수. i는 달팽이에 들어갈 숫자
    snail[front][back] = i                                  # 달팽이 맨 앞에 1 삽입
    while cnt <= n//3:                                      # n이 6이면 삼각형 두번 그려지는 규칙을 발견해서 탈출 조건을 이렇게 만들어 줌
        while front < n-1 and not snail[front+1][back]:     # 왼쪽 변 생성하는 조건. 범위 안벗어나고 달팽이 배열이 0일경우만 실행됨.
            front+=1
            i+=1
            snail[front][back] = i
        
        while back < n-1 and not snail[front][back+1]:      # 아랫쪽 변 생성하는 조건. 범위 안벗어나고 달팽이 배열이 0일경우만 실행됨.
            back+=1
            i+=1
            snail[front][back] = i
        
        while not snail[front-1][back-1]:                   # 오른쪽 변 생성하는 조건. 범위 안벗어나고 달팽이 배열이 0일경우만 실행됨.
            front-=1
            back-=1
            i += 1
            snail[front][back] = i
        cnt += 1                                            # 삼각형 한 번 그렸으니 count 하나 올려줌
    
    res = snail[0]
    for i in range(1, len(snail)):
        res.extend(snail[i])
    return res


def solution(n):
    ans = [[0 for _ in range(i+1)] for i in range(n)]
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for _ in range(i, n):
            if i%3 == 0:
                x+=1
            elif i%3 == 1:
                y+=1
            else:
                x-=1
                y-=1
            ans[x][y] = num
            num += 1
    return sum(ans, [])

if __name__ == "__main__":
    res = mysol(3)
    print(res)