'''OX퀴즈'''
for _ in range(int(input())):
    sum, i = 0, 0
    ans = input()
    for a in ans:
        if a == 'O':
            i += 1
            sum += i
        elif a == 'X':
            i = 0
    print(sum)

