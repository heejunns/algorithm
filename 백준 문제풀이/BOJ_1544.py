# 백준 1544번, 사이클 단어
import sys
from collections import deque
n = int(sys.stdin.readline()) # 단어의 개수 n 입력받기
input_list = [] # 입력받는 문자열을 저장 할 리스트
str_count = 0 # 서로 다른 단어의 개수를 세는 변수
for i in range(n): # 단어 입력 받기
    input_str = sys.stdin.readline().rstrip()
    input_list.append(input_str)
while len(input_list) > 0: # 입력받은 단어의 리스트의 길이가 0 이 될때까지
    str_count+=1 # 서로 다른 단어 개수 +1
    str_pop = input_list.pop() # 단어 하나 꺼내기
    str_pop_list = deque(list(str_pop)) # 리스트, deque 로 변환
    for i in range(len(str_pop_list)): 
        while True: # 중복되는 같은 단어가 있을 수 있기 때문에 없을때까지 input_list 에서 꺼내기
            if("".join(str_pop_list) in input_list): 
                input_list.pop(input_list.index("".join(str_pop_list)))
            else:
                break
        # 꺼낸 단어의 왼쪽에서 문자 하나를 꺼내 오른쪽으로 붙이기
        new_str_list = str_pop_list.popleft()
        str_pop_list.append(new_str_list)
print(str_count)


