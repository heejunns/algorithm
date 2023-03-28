# 백준 11478번, 서로 다른 부분 문자열의 개수
import sys
s = sys.stdin.readline().strip() # 문자열 s 입력받기
result = {} # 부분 문자열을 저장할 dict, 자동으로 중복되는 문자열은 저장이 되지 않음
for i in range(1,len(s)+1): # 부분 문자열 만들기, i 에 따라서 부분 문자열의 개수가 달라짐
    index_1 = 0
    index_2 = i
    while index_2 < len(s)+1: # index_2 가 입력받은 문자열의 길이보다 1 이 크다면 s 문자열로 만들 수 있는 부분 문자열을 모두 만들었다는 뜻이니까 while 문 탈출
        result[s[index_1:index_2]] = 0 # 부분 문자열로 등록
        index_1+=1
        index_2+=1
print(len(result))

