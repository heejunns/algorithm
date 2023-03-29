# 백준 5430번, AC
import sys
from collections import deque
n = int(sys.stdin.readline()) # 테스트 케이스의 개수 n 입력받기
result = [] # 각 테스트 케이스의 결과를 저장할 리스트
for i in range(n): 
    input_function = sys.stdin.readline().rstrip() # 테스트 케이스에서 수행할 함수
    list_number = int(sys.stdin.readline()) # 배열에 들어있는 수의 개수
    input_list_str = sys.stdin.readline().rstrip()[1:-1] # 배열에 들어있는 정수 입력받기

    if input_list_str == "": # 입력받은 배열의 정수 문자열에서 양 끝에 [] 를 제거한 문자열에 따라서 list 만들기
        input_list = deque([])
    else:
        input_list = deque(input_list_str.split(","))

    reverse_count = 0 # 입력받은 수행할 함수에서 뒤집기의 개수를 세는 변수
    yes_error = False # 각 테스트 케이스에서 error 가 발생했는지의 여부를 저장할 변수
    for l in input_function:
        if l == "R":
            reverse_count+=1 # 뒤집기 개수 +1
        elif l == "D": # 첫번째 수를 버리기
            if len(input_list) == 0: # 각 테스트 케이스의 리스트의 길이가 0 이라면 error
                result.append("error")
                yes_error = True
                break
            elif reverse_count%2 == 0: # 뒤집기의 개수가 2 로 나눈 나머지가 0 이라면
                input_list.popleft() # 맨 앞의 값 제거
            else: # 뒤집기의 개수가 2 로 나눈 나머지가 0 이 아니라면
                input_list.pop() # 맨 끝 값 제거
    if (not yes_error): # error 가 발생하지 않았다면
        if reverse_count%2 == 0: # 뒤집기의 개수가 2 로 나눈 나머지가 0 이라면
            result.append("["+",".join(input_list)+"]")
        elif reverse_count%2 == 1: # 뒤집기의 개수가 2 로 나눈 나머지가 1 이라면
            input_list.reverse() # 뒤집기
            result.append("["+",".join(input_list)+"]")

for i in result:
    print(i)
