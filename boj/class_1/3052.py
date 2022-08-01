from collections import Counter
print(len(Counter([int(input())%42 for _ in range(10)])))