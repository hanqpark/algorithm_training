# https://leetcode.com/problems/utf-8-validation/

def check(size, start):
    for i in range(start+1, start+size+1):
        if i>= len(data) or (data[i] >> 6) != 0b10:
            return False
    return True
        
def validUtf8(data):
    start = 0
    while start < len(data):
        first = data[start]
        if first>>3 == 0b11110 and check(3, start):
            start += 4
        elif first>>4 == 0b1110 and check(2, start):
            start += 3
        elif first>>5 == 0b110 and check(1, start):
            start += 2
        elif first>>7 == 0:
            start += 1
        else:
            return False
    return True


if __name__ == "__main__":
    data = [235,140,4]
    print(validUtf8(data))