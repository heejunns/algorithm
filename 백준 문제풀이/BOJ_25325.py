# 백준 25325, 학생 인기도 측정
import sys
n = int(sys.stdin.readline()) # 학생 수 n 입력받기
a_list = list(map(str,sys.stdin.readline().rstrip().split())) # 학생 이름 입력받기
a_dict = {} # 각각의 학생의 인기도를 기록할 dict
for i in a_list:
    a_dict[i] = 0 # 학생의 이름을 키로 dict 에 저장, value 는 0 
for l in range(n):
    inputs = list(map(str,sys.stdin.readline().rstrip().split())) # 각각의 학생이 좋아하는 이름 입력받기
    for k in inputs: # dict 에 인기도 저장
        a_dict[k]+=1
a_dict_value = list(a_dict.values()) # a_dict 의 value 값만 꺼내서 list 만들기
a_dict_value.sort() # 오름차순으로 정렬하기
result = [] # 결과를 저장할 리스트
while len(result) < n: # result 의 길이가 n 개가 될 때까지
    for l in a_list: # a_list 를 꺼내서
        if a_dict[l] == a_dict_value[-1]: # 가장 큰 값에 해당하는 a_dict 의 key 찾기
            result.append(l+" "+str(a_dict[l])) # result 에 저장
            a_dict_value.pop() # 꺼내기
            a_list.pop(a_list.index(l)) # a_list 에 해당하는 값도 꺼내기
            break # 반복문 종료
for i in result:
    print(i)



    
