# 프로그래머스 완주하지 못한 선수 (level 1)
from collections import Counter 
def solution(participant, completion):
    answer = ""
    x = Counter(participant)
    y = Counter(completion)
    for i in participant:
        if y.get(i) == None:
            answer = i
            break
        elif x.get(i) != y.get(i):
            answer = i
            break
    return answer

    
