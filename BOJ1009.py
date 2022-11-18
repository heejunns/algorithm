# BOJ 1009 분산처리
# 주어지는 b의 제곱을 모두 제곱하여 10으로 나누고 그 나머지 값을 마지막 데이터를 처리하는 컴퓨터번호로 해결할려고 했지만 시간 초과가 발생.
# 고민해보니 4제곱 간격으로 일의자리수가 반복되는 것을 알아내고 문제 해결 
import sys 
n = int(sys.stdin.readline())
result = []
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    if b%4 == 0: # 제곱이 4마다 일의자리수가 반복된다. 다 제곱을 할 이유가 없음. 4로 나누어 떨어진다면 4 제곱을 넣어주기 위해 나누어 떨어지는 값을 if문으로 찾는다. 
        if (a**(4))%10 == 0: # 10으로 나누었을때 나머지가 0이면 되면 10을 넣어준다. 
            result.append(10)
        elif (a**(4))%10 > 0: 
            result.append((a**(4))%10) # 10으로 나누어 떨어지는 값 말고는 나머지가 마지막 데이터를 처리하는 컴퓨터의 번호이다. 
    else: # 4로 나누어 떨어지는 값이 아니면 나머지 값으로 제곱한다. 
        if (a**(b%4))%10 == 0: 
            result.append(10)
        elif (a**(b%4))%10 > 0:
            result.append((a**(b%4))%10)
for k in result:
    print(k)
        