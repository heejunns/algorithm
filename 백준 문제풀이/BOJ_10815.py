# 백준 10815번, 숫자 카드 , dict 자료형을 이용 
import sys
n = int(sys.stdin.readline()) # 상근이가 가지고 있는 카드의 개수
n_list = list(map(int,sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().rstrip().split()))
result_dict = {} 
for i in n_list: # 상근이가 가지고 있는 카드를 n_list 를 result_dict 에 key 값으로 채워 넣기
    result_dict[i] = 0 # 값은 임의의 수 0 으로 설정
for l in range(m): # m 개의 카드를 한개씩 꺼내서ㅓ result_dict 에 있는지 확인 
    if m_list[l] in result_dict:
        print(1, end = " ")
    else : 
        print(0, end = " ")