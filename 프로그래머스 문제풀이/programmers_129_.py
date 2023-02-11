# 프로그래머스 문자열 내림차순으로 배치하기 (level 1)
from string import ascii_uppercase
def solution(s):
    answer = ""
    x_upper = []
    x_lower = []
    for i in s:
        if i in ascii_uppercase: # 대문자이면 
            x_upper.append(i)
        else: # 소문자이면
            x_lower.append(i)
    x_upper.sort(reverse=True) # 반대로 정렬
    x_lower.sort(reverse=True)
    x_lower.extend(x_upper) # 하나의 리스트로 확장
    return "".join(x_lower) # join 함수로 문자열 만들어서 반환
