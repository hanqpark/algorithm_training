def solution(arr1, arr2):
    ans = []
    for row in arr1:
        lst = []
        for idx in range(len(arr2[0])):
            lst.append(sum([r*arr2[i][idx] for i, r in enumerate(row)]))
        ans.append(lst)
    return ans


def using_zip(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]