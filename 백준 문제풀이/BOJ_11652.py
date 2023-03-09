# 백준 11652 번, 카드
import sys
n = int(sys.stdin.readline()) # 숫자 카드 개수 n 입력받기
total = [int(sys.stdin.readline()) for i in range(n)] # n 개의 카드를 각각 입력받기
total.sort() # 오름차순으로 정렬 
total_dict = {} # total 을 dict 으로 생성하기 위한 dict
for i in total: # total 을 하나씩 꺼내서 dict 만들기
    if i not in total_dict:
        total_dict[i] = 1
    else:
        total_dict[i]+=1
max_key = 0 # value 가 가장 큰 key 값
max_value = 0 # 가장 큰 value 값
for l in total_dict: # total_dict 에서 key 를 하나 꺼내기
    if total_dict[l] > max_value: # max_value 보다 현재 꺼낸 key 의 value 가 크다면
        max_value = total_dict[l] # 현재 꺼낸 key 에 해당하는 value 를 max_value 에 저장
        max_key = l # 현재 꺼낸 key 를 max_key 에 저장
print(max_key)