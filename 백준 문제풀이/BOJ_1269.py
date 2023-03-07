# 백준 1269번, 대칭 차집합
import sys
a,b  = map(int,sys.stdin.readline().rstrip().split()) # a,b 원소의 개수 입력받기
input_a_list = list(map(int,sys.stdin.readline().rstrip().split())) # a 집합의 원소 입력받기
input_a_dict = {}
for l in input_a_list: # a 집합 요소로 dict 생성
    input_a_dict[l] = 0 # 값은 임의의 값 0 지정 
input_b_list = list(map(int,sys.stdin.readline().rstrip().split())) # b 집합의 원소 입력받기
for i in input_b_list: # b 집합의 원소 한개씩 반복
    if i in input_a_dict: # i 가 a 집합 dict 에 있다면
        del input_a_dict[i] # a 집합 dict 에서 i 요소에 해당하는 요소 제거
    else: # i 가 a 집합 dict 에 없다면
        input_a_dict[i] = 0  # a 집합 dict 에 i 요소 추가
print(len(input_a_dict))
