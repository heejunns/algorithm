# 백준 17413번, 단어 뒤집기 2
import sys
from collections import deque
str = sys.stdin.readline().strip() # 문자열 s 입력받기

change_str = str.split() # 단어 변환을 위해서 입력 받은 문자열을 공백 기준으로 나누기
change_result_str = "" # 변환된 문자열들을 저장할 변수
char = "" # 변환 될 단어들을 저장할 변수

check = False # "<", ">" 문자가 시작되었고 끝나는것을 확인하기 위한 변수, 
# false 라는 뜻은 "<" 를 만나 아직 ">" 를 만나지 않았다는 뜻이다.

result_str = list(str) # 입력 받은 문자열을 공백 포함 모두 하나의 원소로 쪼갠 리스트
# 이 리스트는 위에서 공백을 기준으로 쪼갠 문자열들과 비교하여 공백을 넣어주기 위해 필요한 리스트이다.
final_result = "" # 최종 변환된 문자열의 결과를 저장 할 리스트

for i in change_str: 
    for j in  i:
        if check == False and j == "<": # check 가 false 이고 j 가 "<" 라면
            if len(char) != 0: # 기존의 변화 할 단어가 있었는지 체크
                a = list(char)
                a.reverse()
                change_result_str+= ("".join(a))
                char = ""
            change_result_str+=j
            check = True # "<" 를 만났으니 check 를 true 로 변환
        elif check == True and j !=">": # check 가 true 인데 j 가 ">" 가 아니라면 문자는 그대로 저장
            change_result_str+=j
        elif check == True and j == ">": # check 가 true 인데 j 가 ">" 라면
            change_result_str+=j
            check = False # check 를 false 로 변경
        elif check == False: # check 가 false 라면 변경해야 할 문자니까 저장
            char+=j
    if (len(char)!=0): # 변환해야할 단어가 있다면
        b =  list(char)
        b.reverse()
        change_result_str+=("".join(b))
        char = ""
result = deque(list(change_result_str)) # 변환한 문자열을 하나씩 쪼개기
for i in result_str: # 입력받은 문자열을 모두 쪼갠 요소들을 하나씩 꺼내기
    if i == " ": # i 가 공백일때
        final_result+=i 
    else: # i 가 공백이 아닐떄
        final_result+= result.popleft() # 변환한 문자열을 쪼갠 리스트의 왼쪽 요소를 꺼내기
print(final_result)



