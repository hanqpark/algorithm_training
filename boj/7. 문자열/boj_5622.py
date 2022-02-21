'''다이얼'''
alphabet = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
sum = 0
for c in input():
    for idx, a in enumerate(alphabet):
        if c in a:
            sum += idx+3
print(sum)
