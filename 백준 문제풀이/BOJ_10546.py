# 백준 10546번, 배부른 마라토너
import sys
n = int(sys.stdin.readline()) # 참가자 수 n 입력받기
marathon_participant_dict = {} # 마라톤 참가자를 dict 에 저장하기 
for i in range(n):
    marathon_participant = sys.stdin.readline().rstrip() # 각각의 마라톤 참가자 이름 입력받기
    if marathon_participant not in marathon_participant_dict: # 마라톤 참가자가 dict 에 없다면
       marathon_participant_dict[marathon_participant] = 1 # dict 에 추가
    else: # 마라톤 참가자 dict 에 있다면 동명이인 이라는 뜻 이니까 +1
        marathon_participant_dict[marathon_participant]+=1
for j in range(n-1): # 마라톤 완주자 입력
    marathon_completion = sys.stdin.readline().rstrip() # 각각의 마라톤 완주자 입력받기
    if marathon_participant_dict[marathon_completion] == 1: # 각각의 마라톤 완주자가 마라톤 참가자 dict 에서 value 값이 1 이라면
        del marathon_participant_dict[marathon_completion] # dict 에서 삭제
    elif marathon_participant_dict[marathon_completion] > 1: # 1 보다 크다면 동명이인이 있다는 뜻 이니까
        marathon_participant_dict[marathon_completion]-=1 # 마라톤 완주자 이름에 해당하는 value 값 -1
print(list(marathon_participant_dict.keys())[0]) # dict 에 남은 사람이 마라톤을 완주하지 못한 사람 이니까 key 값 출력하기