# 220831
# BOJ 1107번 리모컨
# 난이도: 골드 5
# https://www.acmicpc.net/problem/1107

from collections import deque

def bfs():
    # 희망 채널을 +1, -1 하며 가장 가까운 채널 번호 찾기
    dq = deque([[n, 0]])
    while dq:
        now, cnt = dq.popleft()
        # 100번에서 이동하는 것보다 느리면 끊어주기
        if cnt+len(str(now)) > abs(n-100):
            return abs(n-100)
        # 탐색 중인 채널 번호에 망가진 버튼이 있으면 다음으로 넘어가기
        success = True
        for num in set(str(now)):
            if num in buttons:
                success = False
                if 0 < now <= n: dq.append([now-1, cnt+1])
                if now >= n: dq.append([now+1, cnt+1])
                break
        # 그렇지 않으면 그 채널 번호 넘겨주기
        if success:
            return cnt+len(str(now))

if __name__ == "__main__":
    n, m = int(input()), int(input())
    buttons = input().split() if m else list()  # m이 0일때 input 안받음...낚임ㅋㅋ
    print(bfs())
