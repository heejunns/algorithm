# 백준 1181번 , 단어 정렬
import sys
n = int(sys.stdin.readline()) # 단어의 개수 입력받기

input = [] # 압력받은 단어를 저장 할 리스트

for i in range(n): # 단어 입력받기
    text = sys.stdin.readline().rstrip()
    input.append(text)

input = list(set(input)) # 중복되는 단어를 제거하기 위해서 set 으로 변경 후 다시 리스트로 변경

result = [] # 정렬 결과를 저장 할 리스트

while len(input) > 1:
    before_result = [] # 정렬 결과 리스트에 저장하기 전에 저장 할 리스트
    min_len = 0 # 아직 정렬되지 않은 단어들 중 가장 길이가 짧은 단어의 길이를 저장 할 변수
    for i in input:
        if len(before_result) == 0: # 처음에는 before_result 리스트에 아무것도 없으니까 저장
            before_result.append(i)
            min_len = len(i)
        elif len(i) < min_len: # 저장되어 있는 가장 짧은 단어의 길이보다 더 짧다면
            before_result = []
            before_result.append(i)
            min_len = len(i)
        elif len(i) == min_len: # 저장되어 있는 가장 짧은 단어의 길이와 같다면
            before_result.append(i)
    for k in before_result: # 현재 뽑은 단어들 input 에서 꺼내기
        input.pop(input.index(k))
    if len(before_result) > 1: # 뽑은 단어가 1개 이상이라면 사전순으로 정렬
        before_result.sort()
    result.extend(before_result) # 정렬 결과 리스트에 정렬한 리스트를 넣기
result.extend(input) # 마지막 남은 단어를 정렬 결과 리스트에 저장
for i in result: # 하나씩 정렬 결과 단어 출력
    print(i)
