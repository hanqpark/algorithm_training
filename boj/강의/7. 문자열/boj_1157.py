'''단어 공부'''
string = input().lower()
max = ['', 0]
for s in set(string):
    cnt = string.count(s)
    if max[-1] < cnt:
        max = [s, cnt]
    elif max[-1] == cnt:
        max.append(s)
        max.append(cnt)
if len(max) > 2:
    print("?")
else:
    print(max[0].upper())