# https://leetcode.com/problems/merge-intervals

from collections import deque

def merge(intervals):
    intervals, answer = deque(sorted(intervals)), list()
    while intervals:
        try:
            left = intervals.popleft()
            right = intervals.popleft()
            if left[1] >= right[0]:
                new = [left[0], max(left[1], right[1])]
                intervals.appendleft(new)
            else:
                answer.append(left)
                intervals.appendleft(right)
        except IndexError:
            answer.append(left)
            return answer