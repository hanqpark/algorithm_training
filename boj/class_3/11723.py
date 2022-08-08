import sys
read = sys.stdin.readline

if __name__ == "__main__":
    s = set()
    for _ in range(int(read())):
        y = read().split()
        if y[0] == "add":
            s.add(int(y[1]))
        elif y[0] == "remove":
            if int(y[1]) in s: s.remove(int(y[1]))
        elif y[0] == "check":
            res = 1 if int(y[1]) in s else 0
            print(res)
        elif y[0] == "toggle":
            if int(y[1]) in s: s.remove(int(y[1]))
            else: s.add(int(y[1]))
        elif y[0] == "all":
            s = set(i for i in range(1, 21))
        elif y[0] == "empty":
            s = set()