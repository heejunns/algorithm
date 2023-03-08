# 백준 1302 번, 베스트셀러
import sys
n = int(sys.stdin.readline()) # 팔린 책의 개수 n 입력받기 
inputs_arr = [sys.stdin.readline().rstrip() for i in range(n)] # n 개의 책 이름 입력받기
# 1위가 1개가 아니라면 그 중 사전순에서 제일 앞에 있는 책을 출력해야 한다.
element_max = "" # 가장 많이 팔린 책의 이름 저장할 변수
element_max_value = 0 # 가장 많이 팔린 책의 최대 개수를 저장할 변수
inputs_arr.sort() # 입력받은 책의 이름 사전순으로 정렬

for i in inputs_arr: 
    if inputs_arr.count(i) > element_max_value: # 책의 이름을 저장한 리스트에서 하나씩 꺼내어 그 책의 이름을 가진 책의 개수가 최대ㅐ 값보다 크다면
        element_max_value = inputs_arr.count(i) # 최대 값 변경
        element_max = i # 가장 많이 팔린 책의 이름 저장

print(element_max)




