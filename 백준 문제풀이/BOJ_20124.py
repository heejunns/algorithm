# 백준 20124번 , 모르고리즘 회장님 추천 받습니다.
import sys
n = int(sys.stdin.readline()) # 대회를 치른 사람의 수 입력받기
high_grade_list = [] # 가장 높은 점수를 받은 사람의 이름을 저장할 리스트
high_grade = 0 # 가장 높은 점수를 기록할 변수
for i in range(n):
    name,grade = map(str, sys.stdin.readline().rstrip().split()) # 이름과 점수를 입력받기
    if len(high_grade_list) == 0 : # 첫번째 입력받을때 점수가 가장 높은 사람은 첫번째 입력 받은 사람이 된다.
        high_grade = int(grade) 
    elif int(grade) > high_grade: # 현재 저장되어 있는 가장 높은 점수보다 현재 입력받은 점수가 크다면
        high_grade_list = []  # 명단 비우기
        high_grade_list.append(name) # 이름 입력받기
        high_grade = int(grade) # 가장 높은 점수 변경
    elif int(grade) == high_grade: # 현재 저장되어 있는 가장 높은 점수와 같다면
        high_grade_list.append(name) # 이름 입력받기 
if len(high_grade_list) == 1: # 가장 높은 점수를 받은 사람이 한명으로 유일하다면
    print(high_grade_list[0])
else: # 가장 높은 점수를 받은 사람이 한명이 아니라면
    high_grade_list.sort() # 사전순으로 정렬
    print(high_grade_list[0]) # 가장 빠른사람 출력