# BOJ 14919 사과와 바나나 나눠주기 
a,b = map(int,input().split()) # 사과 a, 바나나 b 입력 받기 
if a<=b: # a,b 둘중 작은 값까지 인원수로 나누기 , 두개를 동시에 나머지가 없이 나눠줘야 하기 때문에 작은 값으로 나눠줄 때 나머지가 0인 값인 동시에 큰 값도 0인 공통적인거 찾기 
    for i in range(1,a+1):
        if a%i == 0 and b%i == 0: # 그러면서 둘다 나눴을때 0인 값만 출력 
            print(i,a//i,b//i)
elif a>b:
    for k in range(1,b+1):
        if a%k == 0 and b%k == 0:
            print(k,a//k,b//k)
