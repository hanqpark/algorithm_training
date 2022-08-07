n = int(input())
string = input()
hash = 0
for i, s in enumerate(string):
    hash += (ord(s)-96)*pow(31, i)
print(hash%1234567891)