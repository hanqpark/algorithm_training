while True:
    n = input()
    if n=="0": break
    res = "yes" if n == n[::-1] else "no"
    print(res)