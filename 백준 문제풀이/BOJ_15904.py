# 백준 15904번, UCPC는 무엇의 약자일까?
# 사실 문제는 딱히 어렵지 않았는데 예상하지 못한 반례가 있었습니다.
# 입력받은 문자열 안에 각각의 단어에 제일 앞에 문자만 대문자일거라고 생각했는데
# 한 단어에 한번에 UCPC 가 입력될 수 있고
# 또 입력받은 문자열의 대문자를 모두 꺼내보면 UCCPC , UCPCC 처럼 있을 수 있기 때문에 여기서 UCCP 를 만들 수 있는지 판단 해줘야 합니다.
import sys
big_char = [] # 입력받은 문자얄의 대문자를 저장할 리스트
result = [] # UCPC 를 만들 리스트
input_str = sys.stdin.readline().rstrip() # 문자열 입력받기
for i in input_str: # 입력받은 문자열을 하나씩 꺼내어 대문자만 result 에 저장하기
    if i == i.upper():
        big_char.append(i)
for j in big_char: # 대문자를 하나씩 꺼내어 UCPC 만들기
    if len(result) == 0 and j == "U":
        result.append(j)
    elif len(result) == 1 and j == "C":
        result.append(j)
    elif len(result) == 2 and j == "P":
        result.append(j)
    elif len(result) == 3 and j == "C":
        result.append(j)
if len(result) == 4: # result 의 길이가 4 라면 UCPC 를 만들 수 있다는 뜻이다.
    print("I love UCPC")
else:
    print("I hate UCPC")


