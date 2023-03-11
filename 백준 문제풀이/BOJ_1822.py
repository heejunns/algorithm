# 백준 1822 번, 차집합
import sys
a,b = map(int,sys.stdin.readline().rstrip().split()) # 집합 A,B 의 개수 입력받기
a_list = list(map(int,sys.stdin.readline().rstrip().split())) # 집합 A의 원소 입력받기
b_list = list(map(int,sys.stdin.readline().rstrip().split())) # 집합 B의 원소 입력받기
b_dict = {} # 집합 B 를 dict 으로 생성하기
result = [] # 집합 A에는 속하지만 집합 B 에 속하지 않는 원소들을 저장할 리스트
for k in b_list: # 집합 B의 원소들이 key 값으로 dict 생성 value 는 임의의 수 0 지정
    b_dict[k] = 0
for i in a_list: # 집합 A의 원소들을 하나씩 꺼내서 
    if i not in b_dict: # 집합 B dict 에 없다면 
        result.append(i) # result 리스트에 요소 추가

if (len(result) == 0): # result 리스트의 길이가 0 이라면 집합 A 의 원소가 집합 B 에 모두 속한다는 뜻이니까 
    print(0)
    result.sort()  # result 의 원소를 증가하는 순서로 출력하기 위해서 오름차순으로 정렬ㄴ
else: # 아니라면 집합 A 의 원소중에서 집합 B 에 속하지 않는 원소가 있다는 뜻이니까
    print(len(result))
    for j in result:
        print(j, end = " ")


