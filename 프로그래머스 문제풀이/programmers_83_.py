# 프로그래머스 폰켓몬 (level 1)
def solution(nums):
    answer = 0
    x = []
    for i in nums:
        if i not in x:
            x.append(i)
    if len(nums)//2 >= len(x):
        answer = len(x)
    elif len(nums)//2 < len(x):
        answer = len(nums)//2
    return answer