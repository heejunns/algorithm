# 백준 25593번 , 근무 지옥에 빠진 푸앙이 (small)
import sys
n = int(sys.stdin.readline()) # 근무 주 N 입력받기
remember = {}
def calculator(x,j) :
    k = 4 # 기본 값을 4시간으로 지정, 1,3 번째 시간대 
    if(j == 2): # 2번째 시간대라면
        k = 6
    elif (j == 4): # 3번째 시간대라면
        k = 10
    for l in x: # 일주일동안 같은 시간대의 근무표를 하나씩 꺼내기
        if l != "-": # - 가 아니라면
            if l not in remember: # l 이 remember 에 없다면
                remember[l] = k  # 등록
            elif l in remember: # l 이 remember 에 있다면
                remember[l] += k  # 기존의 근무 시간과 더하기
for i in range(n): # 근무 주의 근무표 입력 받기
    for j in range(1,5): # 일주일동안 각각 시간대의 일주일 근무표 받기, 근무 시간대는 4개
        x = list(map(str, sys.stdin.readline().rstrip().split())) # 일주일동안 같은 시간대의 근무표 입력 받기
        calculator(x,j)
result = list(remember.values()) # rememeber 의 값들만 모두 가져와 list 로 형 변환
if result == []: # 아무도 근무하지 않았을 경우 
    print("Yes")
elif (max(result)-min(result) < 13): # 가장 많이 근무한 사람과 가장 적게 근무한 사람의 차가 13 보다 작을 경우 모든 근무자의 근무 시간이 12 이하로 차이 나니까
    print("Yes")
else:
    print("No")

           

        
