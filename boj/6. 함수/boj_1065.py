'''한수'''

hansu = [True for _ in range(1000)]
hansu[0] = False
for i in range(100, 1000):
    one = i%10
    ten = i//10%10
    hund = i//100
    if hund-ten != ten-one:
        hansu[i] = False

print(hansu[:int(input())+1].count(True))

