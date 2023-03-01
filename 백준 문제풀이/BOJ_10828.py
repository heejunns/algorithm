# 백준 10828번, 스택
import sys
n = int(sys.stdin.readline()) # 명령의 수 입력 받기
total = [] # 스택
result = [] # 스택에서 명령에 의해 출력되는 정수들 저장
for i in range(n):
    inputs = list(map(str,sys.stdin.readline().rstrip().split()))
    if(inputs[0] == "push"):
        total.append(int(inputs[1]))
    elif(inputs[0] == "pop"):
        if(len(total) > 0):
            result.append(total.pop())
        else:
            result.append(-1)
    elif (inputs[0] == "size"):
        result.append(len(total))
    elif (inputs[0] == "empty"):
        if(len(total) == 0):
            result.append(1)
        else:
            result.append(0)
    elif (inputs[0] == "top"):
        if(len(total) > 0):
            result.append(total[-1])
        else : 
            result.append(-1)
for l in result:
    print(l)
        

