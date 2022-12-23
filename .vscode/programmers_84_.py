# 프로그래머스 등수 매기기 (level 0)
def solution(score):
    x = [] # 영어, 수학 점수의 합을 기록할 리스트 
    answer = [0]*len(score) # 등수를 기록할 리스트 
    remember = 0 # 큰 값을 찾아낼때 이전 값 기록할 변수 
    for i in score:
        x.append(sum(i)) # 점수의 합 리스트 만들기 
    for l in range(1,len(x)+1): # 등수 부여하기 
        m = max(x)
        if remember == m: # 전에 값과 같다면 
            answer[x.index(m)]  = n # 저장한 등수 계속 사용
        else:
            answer[x.index(m)] = l
            n = l # 등수 기록 
        remember = m # 전에 값 기록 
        x[x.index(m)] = -1  # 처리한 점수는 -1로 처리하기 

    return answer
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))