# 프로그래머스 가장 가까운 같은 글자 (level 1)
def solution(s):
    answer = [] # 결과를 저장할 리스트 
    x = [] # s 문자열의 각각의 문자를 저장할 리스트
    for i in s:
        if i not in x: # x에 없다면 -1 을 저장
            answer.append(-1) 
        else: # x에 있다면 
            x.reverse() # 가장 가까운 가까운 문자가 몇칸 차이나는지 확인하기 위해서 뒤집기 
            n = x.index(i)
            answer.append(n+1) # 인덱스가 0부터 시작하니까 +1 해주기
            x.reverse()     # 다시 뒤집어두기 
        x.append(i) # 모든 문자를 저장
            
    return answer