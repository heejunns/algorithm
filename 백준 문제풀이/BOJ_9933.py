# 백준 9933 번 , 민균이의 비밀번호
import sys
n = int(sys.stdin.readline()) # 단어의 수 입력 받기
total = [] # 입력받는 단어를 저장할 리스트
result = 0 # 정답을 저장할 변수
for i in range(n):
    k = sys.stdin.readline().rstrip()
    total.append(k)
for i in total:
    reverse_element = list(i)
    reverse_element.reverse()
    if "".join(reverse_element) in total: # total 의 원소 i 의 뒤집은 문자열이 total 에 존재한다면 정답
        result = i
        break
print(len(result),result[len(result)//2])