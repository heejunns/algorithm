# 백준 1746번 , 듣보잡
import sys
n,m = map(int,sys.stdin.readline().split()) # n,m 의 개수 입력받기
n_dict = {} # n 명의 사람 명단을 저장 할 dict
count = 0 # n, m 명단에 공통 되는 사람을 세기 위한 변수
result = [] # n, m 명단에 공통 되는 사람의 이름을 저장 할 리스트
for i in range(n):
    input_name = sys.stdin.readline().rstrip() # n 명의 명단을 입력받기
    n_dict[input_name] = 0 # 입력 받은 각각의 명단을 dict 에 저장하고 값은 임의의 값 0 으로 저장
for l in range(m):
    input_name = sys.stdin.readline().rstrip() # m 명의 명단을 입력받기
    if input_name in n_dict: # 입력 받은 각각의 명단이 n 명의 명단이 저장된 n_dict 에 있다면 공통되는 사람이다.
        count+=1
        result.append(input_name)
result.sort() # 사전순으로 정렬
print(count)
for k in result:
    print(k)