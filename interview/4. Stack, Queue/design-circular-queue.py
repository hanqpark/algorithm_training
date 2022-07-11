# https://leetcode.com/problems/design-circular-queue/

import collections

class MyCircularQueue:
    
    def __init__(self, k: int):
        self.dq = collections.deque()
        self.dq_len = k

    def enQueue(self, value: int) -> bool:
        if len(self.dq)==self.dq_len:
            return False
        else:
            self.dq.append(value)
            return True

    def deQueue(self) -> bool:
        if not self.dq:
            return False
        else:
            self.dq.popleft()
            return True

    def Front(self) -> int:
        return -1 if not self.dq else self.dq[0]

    def Rear(self) -> int:
        return -1 if not self.dq else self.dq[-1] 

    def isEmpty(self) -> bool:
        return len(self.dq)==0

    def isFull(self) -> bool:
        return len(self.dq)==self.dq_len


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()