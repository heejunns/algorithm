# 백준 1388번 바닥 장식
import sys
n,m = map(int,sys.stdin.readline().rstrip().split()) # 세로 크기 n, 가로 크기 m 입력받기
floor_info = [] # 바닥의 정보를 저장할 리스트
for i in range(n):
    input = list(sys.stdin.readline().strip())
    floor_info.append(input)
count = 0 # 바닥 장식의 개수
for i in range(n): # 가로로 하나씩 바닥의 장식을 꺼내어 "-" 로 되어 있는 나무 판자의 개수 세기
    s = 0 # "|" 가 나오면 "-" 의 하나의 나무 판자인지 구분하기 위해 
    for l in range(m):
        if floor_info[i][l] == "-" and s == 0:
            s = 1
            count+=1
        elif floor_info[i][l] == "|":
            s = 0
for i in range(m): # 세로로 하나씩 바닥의 장식을 꺼내 "|" 로 되어 있는 나무 판자의 개수 세기
    s = 0
    for l in range(n):
        if floor_info[l][i] == "|" and s == 0:
            s = 1
            count+=1
        elif floor_info[l][i] == "-":
            s = 0
print(count)

            
    

