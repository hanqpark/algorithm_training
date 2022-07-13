from collections import Counter

def solution(id_list, report, k):
    answer = []
    
    # 중복 제거
    report = list(set(report))
    
    # report dictionary 생성
    report_dict, report_list = {}, []
    for r in report:
        affend, defence = r.split(" ")
        report_list.append(defence)
        if affend in report_dict:
            report_dict[affend].append(defence)
        else:
            report_dict[affend] = [defence]
    
    # 신고 회수
    report_cnt = Counter(report_list)
    
    # 결과 메일 수
    for i in id_list:
        cnt = 0
        try:
            for d in report_dict[i]:
                if report_cnt[d] >= k:
                    cnt += 1
        except KeyError as e:
            pass
        answer.append(cnt)
        
    
    return answer
    
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))