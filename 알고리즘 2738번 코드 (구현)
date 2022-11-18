a,b = map(int,input().split())
n = 1
m = 1
x = []
y = []
z = 0 
total_result = []
while a>=n: # 첫번째 행렬 값 x 리스트에 저장
    result1 = map(int,input().split())
    x.extend(result1)
    n+=1

while a >=m: # 두번째 행렬 값 y 리스트에 저장 
    result2 = map(int,input().split())
    y.extend(result2)
    m+=1

while (a*b) > z:
    total = x[z] + y[z] # 같은 인데스 값끼리 더하기 
    total_result.append(total)
    z+=1
t = 0
c = 1
y = 0 
while a > t:
    t+=1
    c = 0
    while b > c: # b 의 열 까지 출력 하고 c 가 b의 열이 되면 마지막 출력 후 줄 바꿈 하기 
        if c == (b-1):
            print(total_result[y],end = " ")
            print("")
            y+=1
            c+=1
        else:
            print(total_result[y],end = " ")
            y +=1
            c+=1
 # 구현은 해서 정답은 맞췄지만 코드가 너무 비효율적으로 보인다. 좀 더 효율적인 코드 작성 방법을 생각 해보고 공부 해야겠다. 
