# https://stackoverflow.com/questions/9843033/pythonic-way-to-eval-all-octal-values-in-a-string-as-integers
# https://velog.io/@fstone/정규표현식-정리
# \b : 단어 경계에 대응
# the 0+ matches one or more consecutive zeroes;
# A(?!B) : A 뒤에 B가 없는 경우에만 접근할 수 있다.
import re

def woosung():
    input_text = input().split('-')
    final_result = 0
    count = 0

    for i in input_text:
        nums = map(int, i.split('+'))
        sum_nums = sum(nums)
        
        if count == 0: final_result += sum_nums
        else: final_result -= sum_nums

        count += 1

    print(final_result)


s = list(re.sub(r'\b0+(?!\b)', '', input()))
open = False
for i in range(len(s)+s.count("-")*2-1):
    if s[i] == "-":
        if open:
            s.insert(i, ")")
            open = False
        else:
            s.insert(i+1, "(")
            i += 1
            open = True
if open: s.append(")")
print(eval("".join(s)))
