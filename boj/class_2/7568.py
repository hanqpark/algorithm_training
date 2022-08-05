import sys
read = sys.stdin.readline

def hanq():
    people = []
    n = int(read())
    for i in range(n):
        w, h = map(int, read().split())
        people.append([w, h, i])
    people.sort(reverse=True, key=lambda x: (x[0], x[1]))

    grade = 1
    for i in range(len(people)):
        if i < grade-1: continue
        for j in range(i+1, len(people)):
            if people[i][0] >= people[j][0] and people[i][1] >= people[j][1]:
                break
            people[j].append(grade)
        people[i].append(grade)
        grade += j-i

    people.sort(key=lambda x: x[2])
    res = [str(x[-1]) for x in people]
    print(" ".join(res))
    
def woosung():
    