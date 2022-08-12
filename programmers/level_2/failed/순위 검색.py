def solution_1(info, query):
    lang, stack, career, food, score = [], [], [], [], []
    for i in info:
        l, s, c, f, x = i.split()
        lang.append(l)
        stack.append(s)        
        career.append(c)        
        food.append(f)        
        score.append(x)

    ans = []
    for q in query:
        notcond = q.count("-")
        la, st, ca, tmp = q.split(" and ")
        fo, sc = tmp.split()
        cnt = 0
        for l, s, f, c, x in zip(lang, stack, food, career, score):
            ll = 1 if l==la else 0
            ss = 1 if s==st else 0
            cc = 1 if c==ca else 0
            ff = 1 if f==fo else 0
            xx = 1 if int(x)>=int(sc) else 0
            if ll+ss+cc+ff+xx == 5-notcond: cnt += 1
        ans.append(cnt)
    return ans


def solution_2(info, query):
    ans = []
    for q in query:
        la, st, ca, tmp = q.split(" and ")
        fo, sc = tmp.split()
        qs = [la, st, ca, fo, sc]
        cnt = 0
        for i in info:
            flag = True
            ii = i.split()
            for idx in range(5):
                if qs[idx] == "-": continue
                if idx == 4:
                    if int(ii[idx])<int(qs[idx]): flag=False; break
                else:
                    if ii[idx] != qs[idx]: flag=False; break
            if flag: cnt += 1
        ans.append(cnt)
    return ans