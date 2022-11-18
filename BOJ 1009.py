# boj 1009번 분산 처리 
# 이 문제의 해결 아이디어는 입력되는 a,b로 몇개의 데이터가 들어오는지 a^b를 통해서 구한 후 10으로 나눈 나머지를 리스트에 저장 후 출력하는 아이디어다. 
import sys 
result = []
n = int(sys.stdin.readline())
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    result.append(pow(a,b)% 10)
for k in result:
    print(k)