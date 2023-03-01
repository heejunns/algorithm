# 백준 1920번, 수 찾기
import sys
n = int(sys.stdin.readline()) # n 입력 받기
n_list = list(map(int,sys.stdin.readline().rstrip().split())) # n 개의 정수 입력 받기
m = int(sys.stdin.readline()) # m 입력 받기
m_list = list(map(int,sys.stdin.readline().rstrip().split())) # m 개의 정수 입력 받기
n_dict = {} # n 개의 정수를 dict 으로 저장 할 dict 
for i in n_list:
    n_dict[i] = 1 # n 개의 정수들을 n_dict 에 저장, value 값으로는 임의의 1 저장
for i in m_list: # m 개의 정수들을 하나씩 꺼내기
    if i in n_dict: # i 가 n_dict 에 있다면
        print(1)
    else:
        print(0)