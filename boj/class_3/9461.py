import sys
read = sys.stdin.readline

sam = [1,1,1,2,2,3,4,5,7,9,12,16]
for i in range(12, 101):
    sam.append(sam[i-5]+sam[i-1])
    
for _ in range(int(read())):
    print(sam[int(read())-1])