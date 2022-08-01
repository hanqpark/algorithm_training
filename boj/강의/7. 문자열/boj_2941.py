'''크로아티아 알파벳'''

s = input()
cnt = 0
for i in range(len(s)):
    if s[i] == "-":
        continue
    if s[i] == 'j':
        if s[i-1] =='l' or s[i-1] == 'n':
            continue
    if s[i] == "=":
        if s[i-1] == "z" and s[i-2] == "d":
            cnt -= 1
        continue
    cnt += 1
print(cnt)
