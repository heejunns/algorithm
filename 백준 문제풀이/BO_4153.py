# 백준 4153번 직각삼각형
answer  = [] # 테스트 케이스에 대한 직각 삼각형인지 판단 후 결과 저장
while True:
    x  = list(map(int,input().split())) # 테스트 케이스 입력
    if(sum(x) == 0): # 테스트 케이스의 합이 0 이면 종료
        break
    max_Element = x.pop(x.index(max(x))) # 테스트 케이스 중 제일 큰 값 꺼내기
    if(x[0]**2+x[1]**2) == max_Element**2 : # 테스트 케이스에서 제일 큰 값의 2의 제곱과 나머지 두 값의 2의 제곱 합이 같다면 직각삼각형 
        answer.append("right")
    else : 
        answer.append("wrong")
for i in answer:
    print(i)
