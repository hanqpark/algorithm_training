from collections import deque
from itertools import product

def mysol(numbers, target):
    q = deque([0])
    while numbers:
        number = numbers.pop()
        tmp = []
        while q:
            num = q.popleft()
            tmp.append(num+number)
            tmp.append(num-number)
        q = deque(tmp)
    return q.count(target)
        
    
def solution_2(numbers, target):
    if not numbers:
        return 0 if target else 1
    else:
        return solution_2(numbers[1:], target-numbers[0]) + solution_2(numbers[1:], target+numbers[0])
    

def solution_1(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)


def sangyun(numbers, target):
    answer=0
    stack=[]
    def bfs(numbers,target):
        num_queue=deque(numbers) # numbers가 담아진 큐
        stack.append(num_queue.popleft()) # num_queue 의 첫번째 숫자를 stack 에 넣어준다
        
        
        while num_queue:
            first_num=num_queue.popleft() # 큐에서 첫번째 값 뽑음
            for num in stack:
                stack.append(num+first_num)
                stack.append(num-first_num)
            
        
        return stack
    
    return bfs(numbers,target)