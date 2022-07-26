# https://leetcode.com/problems/k-closest-points-to-origin/

def kClosest(points, k):
    points.sort(key=lambda x: x[0]**2+x[1]**2)
    return points[:k]