import sys
read = sys.stdin.readline

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

if __name__ == "__main__":
    arr = []
    for _ in range(int(read())):
        arr.append(int(read()))
    ans = quick_sort(arr)
    print("\n".join(map(str, ans)))