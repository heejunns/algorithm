# 백준 2751번 , 수 정렬하기 2
import sys
n = int(sys.stdin.readline()) # 수의 개수 입력받기
total = [] # 입력받은 수 저장할 리스트
for i in range(n):
    input_number = int(sys.stdin.readline())
    total.append(input_number)
total.sort() # 오름차순으로 정렬
for l in total : 
    print(l)