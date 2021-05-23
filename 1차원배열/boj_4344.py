'''평균은 넘겠지'''
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr.pop(0)
    avg = sum(arr) / len(arr)
    above_avg = list(map(lambda x: x > avg, arr))
    per = format(round(above_avg.count(True) / len(above_avg) * 100, 3), '.3f')
    print(f'{per}%')

'''
포맷 지정하는 부분 체크
https://andamiro25.tistory.com/16
'''