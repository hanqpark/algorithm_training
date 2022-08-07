def program(bracket, stack):
    for b in bracket:
        if b == "(":
            stack.append(b)
        else:
            if not stack:
                return "NO"
            else:
                stack.pop()
    return "NO" if stack else "YES"

if __name__ == "__main__":
    for _ in range(int(input())):
        bracket, stack = input(), []
        res = program(bracket, stack)
        print(res)