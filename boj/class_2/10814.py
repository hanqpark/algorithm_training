import sys
read = sys.stdin.readline

people = []
n = int(read())
for i in range(n):
    age, name = read().split()
    people.append([int(age), name, i])  # 정렬할 때 int인지 str인지 중요하다     

people.sort(key=lambda x: (x[0], x[2]))
for age, person, i in people:
    print(age, person)