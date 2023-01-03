# 프로그래머스 제일 작은 수 제거하기 (level 1)
def solution(arr):
    arr.pop(arr.index(min(arr))) # 가장 작은수 arr에서 꺼내기
    if arr == []: # arr이 []라면 -1을 추가하기
        arr.append(-1)
    return arr