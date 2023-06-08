# 백준 11650번, 좌표 정렬하기
import sys
n = int(sys.stdin.readline()) # 점의 개수 입력받기
total = {} # 점의 좌표 정보 저장
result = [] # 정렬한 결과 저장
key_list = [] # 입력받은 x 좌표 정보 저장
for i in range(n):
    x,y = map(int,sys.stdin.readline().rstrip().split()) # x, y 좌표 입력받기
    if x not in total : # total 에 x 좌표와 같은 key 가 없다면
        total[x] = [y] # key 로 등록하고 value 값으로는 y 좌표 넣기
        key_list.append(x) # key 값 저장
    else: # 이미 total 에 x 와 같은 key 가 있다면
        total[x].append(y) # value 값에 y 값 추가
key_list.sort() # key 값을 오름차순으로 정렬
for i in key_list: # key 를 하나씩 꺼내기 
    pop_element = total[i] # key 에 해당하는 value 값을 가져오기
    pop_element.sort() # value 값을 오름차순으로 정렬
    for l in pop_element: # 오름차순으로 정렬한 value 값과 key 값을 합쳐 원래 입력 받은 좌표로 만들기
        result.append([i,l]) # result 에 추가
for l in result: # 정렬한 좌표를 출력
    print(l[0],l[1])
