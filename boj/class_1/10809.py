s = input()
for i in range(26):
    try:
        print(s.index(chr(i+97)), end=" ")
    except ValueError:
        print(-1, end=" ")
