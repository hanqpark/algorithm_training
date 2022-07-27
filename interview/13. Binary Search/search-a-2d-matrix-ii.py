# https://leetcode.com/problems/search-a-2d-matrix-ii/

def solution(matrix, target):
    mat = list()
    for m in matrix:
        mat.extend(m)
    return True if target in mat else False

def sol(matrix, target):
    return any(target in row for row in matrix)