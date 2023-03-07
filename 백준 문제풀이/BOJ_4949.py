# 백준 4949번, 균형잡힌 세상
import sys
result = []
while(True):
    input_check = [] # (,),[,] 를 저장할 리스트
    input_str = sys.stdin.readline().rstrip() # 문자열 입력받기
    if input_str == ".": # 입력받은 문자열이 . 라면 종료
        break
    for i in input_str: # 입력받은 문자열을 하나씩 꺼내기
        if i == "(" or i == "[": # 꺼낸 문자가 (, [ 라면 input_check에 저장
            input_check.append(i)
        elif i == ")": # 꺼낸 문자가 ) 이고
            if len(input_check) > 0 and input_check[-1] == "(": # input_check 에 문자가 있고 가장 최근에 저장된 문자가 ( 라면
                input_check.pop() # 가장 최근에 저장된 ( 를 꺼내기
            else : # 아니라면
                input_check.append(i) # ) 를 input_check 에 추가
        elif i == "]": # 꺼낸 문자가 ] 이고 
            if len(input_check) > 0 and input_check[-1] == "[": # input_check 에 문자가 있고 가장 최근에 저장된 문자가 [ 라면
                input_check.pop() # 가장 최근에 저장된 [ 를 꺼내기
            else: # 아니라면
                input_check.append(i) # ] 를 input_check 에 추가
    if len(input_check) == 0: # input_check 에 아무 문자가 없다면
        result.append("yes") 
    else: # input_check 에 문자가 있다면
        result.append("no")
for l in result:
    print(l)
            
