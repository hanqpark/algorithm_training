'''평균'''

import sys
read = sys.stdin.readline

n = int(read())
scores = list(map(int, read().split()))
new_scores = list(map(lambda x: x/max(scores)*100, scores))
print(sum(new_scores) / len(new_scores))

