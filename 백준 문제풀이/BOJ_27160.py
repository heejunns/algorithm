
# 백준 27160번 할리갈리 
import sys
total = {} # 과일의 종류와 개수를 등록할 딕셔너리 생성
n = int(sys.stdin.readline().rstrip()) # 펼쳐진 카드의 개수 
for i in range(n):
    key, value = map(str,sys.stdin.readline().rstrip().split()) # 과일의 정보인 과일의 종류와 개수 입력 받기
    if key in total: # 이미 과일이 등록되어 있다면
        total[key]+=int(value) # 기존의 과일 개수 + 과일 개수
        continue
    total[key] = int(value) # 과일의 종류가 total 에 없다면 등록
if 5 in total.values(): # 과일의 종류들중 개수가 5개인 과일이 있다면
    print("YES")
else:
    print("NO")


