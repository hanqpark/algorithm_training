def solution(n):
    # 변수 선언
    answer, index = [0,3,11], int(n/2)

    # n이 홀수일 경우 -> 0
    if n % 2 != 0: return 0 

    # 3번째까지는 규칙이 없기 때문에 배열에서 return
    if index < 3: return answer[index]
    
    # DP
    for i in range(3, index+1):
    	# answer[i:j] -> answer에서 index가 i인 원소부터 j-1인 원소까지의 sub-array
        answer.append((3*answer[i-1]+sum(answer[1:i-1])*2+2)%1000000007)

    return answer[index]
            