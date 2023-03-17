# 백준 20551번, sort 마스터 배지훈의 후계자
import sys
n,m = map(int, sys.stdin.readline().rstrip().split()) # 배열 a 의 원소의 개수 n, 질문의 개수 m 입력받기
a_list = [int(sys.stdin.readline()) for i in range(n)] # 배열 a 의 원소의 개수 n 개 배열의 원소 입력받기
a_list.sort() # 배열 a 를 오름차순으로 정렬
a_dict = {} # 배열 a 의 원소들을 dict 에 저장할 dict
result_list = [] # 질문의 요소가 배열 a 에 있는지 확인하여 그 결과를 저장할 리스트
for l in range(len(a_list)): 
    if a_list[l] not in a_dict: # 배열 a 의 원소가 a_dict 에 없다면 a_dict 에 저장, 값으로는 해당 원소의 인덱스값으로 저장
        a_dict[a_list[l]] = l
for i in range(m):
    m_input = int(sys.stdin.readline()) # 각각의 질문의 요소를 입력받기
    if m_input in a_dict: # 질문의 요소가 a_dict 에 있다면
        result_list.append(a_dict[m_input])
    else: # 질문의 요소가 a_dict 에 있다면
        result_list.append(-1)
for i in result_list:
    print(i)

