# 백준 14425 번, 문자열 집합
import sys
n,m = map(int, sys.stdin.readline().rstrip().split()) # 문자열의 개수 n, m 입력받기
s_dict = {} # s 집합 dict
count = 0 # m 개의 문자열 중 s 집합에 몇개 포함되는지 세기 위한 변수
for i in range(n): # n 개의 문자열 입력받기
    input_n = sys.stdin.readline().rstrip()
    s_dict[input_n] = 0 # s 집합 dict 에 저장, value 값은 임의의 수 0 저장
for l in range(m): # m 개의 문자열 입력받기
    input_m = sys.stdin.readline().rstrip()
    if input_m in s_dict: # 입력받은 문자열이 s 집합 dict 에 있다면 count +1 
        count+=1
print(count)
