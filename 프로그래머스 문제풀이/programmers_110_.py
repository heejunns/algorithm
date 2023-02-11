# 프로그래머스 하샤드 수 (level 1)
def solution(x):
    answer = True
    total = 0
    for i in str(x): # x를 문자열로 바꿔 
        total+=int(i) # 한자리씩 for문을 반복하여 다시 int형으로 바꿔 모두 더하기
    if x%total != 0: # x를 total로 나누었을때 나머지가 0이 아니면 나누어 떨어지지 않는 것이므로
        answer = False
    return answer