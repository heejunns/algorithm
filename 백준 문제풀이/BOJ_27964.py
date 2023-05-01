# 백준 27964 번, 콰트로 피자
import sys
n = int(sys.stdin.readline()) # 토핑의 개수 입력 받기
pizza = {} # 피자의 치즈 토핑 재료를 저장할 dict
pizzaInput = list(map(str,sys.stdin.readline().rstrip().split())) # 피자 토핑 입력받기
for i in pizzaInput: # 입력받은 피자 토핑 중 토핑 이름의 길이가 6 이상이고 이름 뒤에 Cheese 로 끝나며 현재 pizza 치즈 토핑 dict 에 없는 토핑 재료인지 확인
    if len(i) >=6:
        if(i[-6:] == "Cheese") and i not in pizza:
            pizza[i] = 0 # 치즈 토핑 저장
if len(pizza) >= 4: # 치즈 토핑의 개수가 4개 이상 이라면
    print("yummy")
else:
    print("sad")

