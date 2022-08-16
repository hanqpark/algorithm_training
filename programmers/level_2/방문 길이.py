# 2022.08.16
# https://school.programmers.co.kr/learn/courses/30/lessons/49994
# 방문 길이

xy = {
    "D": (0, 1),
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1)
}

def solution(dirs):
    now = [0,0]
    visited = []
    for d in dirs:
        nx, ny = now            # 현재 좌표
        dx, dy = xy[d]          # 이동할 좌표
        x, y = nx+dx, ny+dy     # 이동한 좌표
        if x in range(-5, 6) and y in range(-5, 6):     # 범위 안에 있으면
            tmp = sorted([now, [x,y]])                  # 1에서 0으로 간 것과 0에서 1로 간 것이 같은 이동 경로이기 때문에 sort해줌
            if tmp not in visited:                      # 이동 경로에 없으면 추가
                visited.append(tmp)
            now = [x, y]                                # 현재 좌표 업데이트
    return len(visited)