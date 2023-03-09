# 백준 3986 번, 좋은 단어 
import sys
n = int(sys.stdin.readline()) # 단어의 수 n 입력받기
good_str = 0 # 좋은 단어의 개수를 세는 변수
for i in range(n):
    input_list = [] # 입력받은 단어의 각각의 문자를 저장할 리스트
    inputs = sys.stdin.readline().rstrip() # 단어 입력받기
    for l in inputs: # 입력받은 단어의 문자를 하나씩 꺼내기
        if input_list == []: # input_list 가 비어 있다면
            input_list.append(l)
        elif l == input_list[-1]: # 현재 꺼낸 문자와 리스트에 저장되어 있는 가장 최근에 추가된 문자가 같다면
            input_list.pop()
        else: # 위의 조건에 해당되지 않는다면
            input_list.append(l)
    if input_list == []: # input_list 가 [] 라면 좋은단어이다.
        good_str+=1
print(good_str)
