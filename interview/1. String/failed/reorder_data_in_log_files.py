# https://leetcode.com/problems/reorder-data-in-log-files/
# 띄어쓰기 보이면 split 잘 활용하도록 하자

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        str_logs, dig_logs = [], []
        for log in logs:
            if log.split()[1].isdigit():    # isalnum -> 문자 or 숫자, isdigit -> 숫자
                dig_logs.append(log)
            else:
                str_logs.append(log)
        str_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        str_logs.extend(dig_logs)
        return str_logs
            