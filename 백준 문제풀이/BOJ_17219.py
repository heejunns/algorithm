# 백준 17219 번, 비밀번호 찾기 , n : 저장된 사이트 주소의 수, m : 비밀번호를 찾으려는 사이트 주소의 수
import sys
n,m  = map(int,sys.stdin.readline().rstrip().split()) # n, m 입력받기
input_dict = {} # 저장된 사이트 주소를 저장할 dict
result = [] # 찾은 비밀번호를 저장할 리스트
for i in range(n):
    inputs = list( map(str,sys.stdin.readline().rstrip().split())) # 사이트 주소와 비밀번호를 입력받기
    input_dict[inputs[0]] = inputs[1] # dict 에 저장
for l in range(m): 
    input_ = sys.stdin.readline().rstrip() # 비밀번호를 찾으려는 사이트 입력받기
    result.append(input_dict[input_]) # 입력받은 찾으려는 사이트에 해당하는 비밀번호를 result 에 저장

for k in result:
    print(k)
