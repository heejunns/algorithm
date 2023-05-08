# 백준 25631번, 마트료시카 합치기
import sys
n = int(sys.stdin.readline()) # 마트료시카 개수 입력받기
input_list = list(map(int,sys.stdin.readline().rstrip().split())) # 각각의 마트료시카의 크기 입력받기
input_list.sort(reverse=True) # 가장 큰 크기의 마트료시카부터 꺼내서 그 안에 그것보다 작은 크기의 마트료시카를 넣기 위해서 내림차순으로 정렬
combine_count = 0 # 마트료시카에 넣어서 한개의 마트료시카로 만든 마트료시카의 개수를 세기 위한 변수

while True :
    current_combine = [] # 현재 합칠려는 마트료시카를 담을 리스트
    count = 0 # 아래의 for 문을 돌 때마다 합칠 수 있는 마트료시카의 개수를 기록하는 변수
    for i in input_list: # 마트료시카를 하나씩 꺼내기
        if len(current_combine) == 0: # 현재 합칠려는 마트료시카의 리스트에 아무것도 없다면
            current_combine.append(i)
        elif current_combine[-1] > i: # 현재 합칠려는 마트료시카의 리스트의 가장 최근의 요소보다 꺼낸 요소가 작다면
            count+=1
            current_combine.append(i)
    if count > 0: # 마트료시카를 합친 개수가 0 보다 크다면
        for l in current_combine: # 원래 주어진 마트료시카에서 그 원소들을 꺼내기
            input_list.pop(input_list.index(l))
    if count == 0: # 가장 최근 for 문을 돌았을 때 합칠 수 있는 마트료시카가 없다면 종료
        break
    combine_count+=1 # 하나로 합친 마트료시카의 개수를 한개 증가
print(combine_count + len(input_list)) # 남아있는 마트료시카의 개수와 합친 마트료시카의 개수를 합친 값을 출력