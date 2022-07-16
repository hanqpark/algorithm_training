
def hanoi(n, dst, arr, tmp):
    if n == 1:
        ans.append([dst, arr])
        return
    
    hanoi(n-1, dst, tmp, arr)
    ans.append([dst, arr])
    hanoi(n-1, tmp, arr, dst)

if __name__ == "__main__":
    ans, n = [], 2
    hanoi(n, 1, 3, 2)
    print(ans)