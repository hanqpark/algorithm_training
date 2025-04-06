# 성공한 솔루션
from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length-1)])
    tw = deque(truck_weights)
    bridge.append(tw.popleft())
    cnt, truck, bw = 1, 0, sum(bridge)
    while bw:
        if tw and not truck:
            truck = tw.popleft()
            
        bw -= bridge.popleft()
        if bw+truck <= weight:
            bridge.append(truck)
            bw += truck
            truck = 0
        else:
            bridge.append(0)
        cnt += 1
    return cnt


# 실패한 솔루션 1 - 하나의 테케에서 안됨
from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length-1)])
    tw = deque(truck_weights)
    bridge.append(tw.popleft())
    cnt, truck = 1, 0
    while sum(bridge):
        if sum(tw) and not truck:
            truck = tw.popleft()
            
        bridge.popleft()
        if sum(bridge)+truck <= weight:
            bridge.append(truck)
            truck = 0
        else:
            bridge.append(0)
        cnt += 1
        # print(bridge)
    return cnt