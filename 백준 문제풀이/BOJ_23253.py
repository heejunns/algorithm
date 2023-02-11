# 백준 자료구조는 정말 최고야 23253번
import sys
n,m = map(int,sys.stdin.readline().rstrip().split()) # 교과서의 수 n, 교과서의 더미 수 m 입력 받기
result = "Yes" # 기본으로 교과서 정리가 된다고 값 두기 정리가 불가 하다면 값 변경
for i in range(m): # 
    a = sys.stdin.readline().rstrip() # 더미의 교과서 수 
    x = list(map(int,sys.stdin.readline().rstrip().split())) # 더미의 교과서 정보
    if x != sorted(x,reverse=True): # 더미의 교과서 정보를 내림차순으로 정렬 했을때 기존의 입력 받은 더미의 교과서 정보와 같은지 비교 
        result = "No" # 아니라면 교과서를 더미 위에서부터 꺼내서 번호 순서대로 정렬이 불가
print(result)