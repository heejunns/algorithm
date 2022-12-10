# 프로그래머스 체육복 (그리디)
def solution(n, lost, reserve):
    lost.sort() # 최대 인원을 뽑아내기 위해 작은 것부터 처리해야 하니까 정리 해주기 
    reserve.sort()
    answer = n - len(lost) # 체육복을 잃어버리지 않은 사람 일단 계산
    remember = [] # lost 와 reserve에 공통적으로 들어가 있는 요소를 기록하는 리스트
    for i in lost:
        if i in reserve:
            remember.append(reserve.pop(reserve.index(i)))
            answer+=1
    for i in remember: # 공통적인 요소 꺼내기
        lost.pop(lost.index(i))
    for i in reserve: # 순서대로 빌려줄 수 있는 요소 찾고 빌려줄 수 있다면 lost에서 꺼내기
        if (i-1) in lost:
            lost.pop(lost.index(i-1))
            answer+=1
        elif (i+1) in lost:
            lost.pop(lost.index(i+1))
            answer+=1
            
    return answer
