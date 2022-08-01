# https://leetcode.com/problems/gas-station/

def sol(gas, cost):
    if sum(gas) < sum(cost): return -1
    
    s, f = 0, 0
    for i in range(len(gas)):
        if gas[i] + f < cost[i]:
            s = i+1
            f = 0
        else:
            f += gas[i]-cost[i]
    return s


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
sol(gas, cost)