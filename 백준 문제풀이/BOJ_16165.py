# 백준 16165번, 걸그룹 마스터 준석이
import sys
n,m = map(int,sys.stdin.readline().split()) # 입력 받은 걸그룹의 수 n, 맞혀야 할 문제의 수 m 입력받기
girl_group = {} # 걸그룹의 이름과 멤버들을 저장할 dice
result = [] # 문제의 정답을 저장할 리스트
for i in range(n):
    girl_group_name = sys.stdin.readline().rstrip() # 걸그룹의 이름 입력받기
    girl_group[girl_group_name] = [] # 걸그룹의 이름을 key 값으로 dict 에 추가 value 값으로는 멤버 이름을 담을 리스트
    girl_group_number = int(sys.stdin.readline()) # 걸그룹 멤버의 수를 입력받기
    for j in range(girl_group_number): 
        girl_group_name_membername = sys.stdin.readline().rstrip() # 걸그룹 멤버의 이름 입력받기
        girl_group[girl_group_name].append(girl_group_name_membername) # 해당 걸그룹에 입력받은 멤버 이름 추가하기
for k in range(m): # 퀴즈 입력받기
    team_or_member = sys.stdin.readline().rstrip() # 팀의 이름이나 멤버의 이름 입력받기
    quiz_mode = int(sys.stdin.readline()) # 퀴즈의 종류 입력받기
    if(quiz_mode == 0): # 퀴즈의 종류가 0 이면
        girl_group_member = girl_group[team_or_member] # 입력 받은 팀의 이름으로 dict 에서 해당하는 팀을 찾고 그 value 값을 저장
        girl_group_member.sort() # 오름차순으로 정렬
        result.extend(girl_group_member) # 결과 리스트에 추가
    elif (quiz_mode == 1): # 퀴즈의 종류가 1 이면
        for i in girl_group: # 입력받은 멤버의 이름이 소속되어 있는 걸그룹을 dict 에서 찾기
            if team_or_member in girl_group[i]:
                result.append(i)
for l in result:
    print(l)