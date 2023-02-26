# 백준 12605 번 , 단어순서 뒤집기
import sys
n = int(sys.stdin.readline()) # 전체 입력받을 케이스 개수
total = [] # 각각의 케이스를 저장할 리스트
for i in range(n):
    s = list(sys.stdin.readline().rstrip().split(" ")) # 각각의 케이스를 공백 단위로 나눠 리스트로 저장
    s.reverse() # 케이스의 요소 순서 뒤집기
    total.append(s) # 저장
for i in range(len(total)):
    print("Case #"+str(i+1)+": "+" ".join(total[i])) # 각각의 케이스 출력
