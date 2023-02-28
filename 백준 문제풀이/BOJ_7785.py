# 백준 7785번 , 회사에 있는 사람
import sys
n = int(sys.stdin.readline()) # 출입 기록 수 n 입력 받기
company = {} # 회사의 기록을 기록할 딕셔너리 생성
for i in range(n):
    a,b = map(str,sys.stdin.readline().rstrip().split()) # 출입 기록 입력 받기
    if a not in company: # company 에 없다면
        company[a] = 1 # company 에 추가, 값은 어떤 값이 들어가도 상관 없어서 임의의 값 1 추가
    else: # company 에 있다면
        del company[a] # company 에 있는데 출입 기록에 또 있다는 것은 퇴근 한다는 뜻이니까 제거
x =list(company) # 딕셔너리 리스트로 변환
x.sort(reverse=True) # 사전 반대 순서로 정렬
for j in x:
     print(j)
