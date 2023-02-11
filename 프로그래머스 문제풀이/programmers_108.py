# 프로그래머스 행렬의 덧셈 (level 1)
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)): # 입력으로 들어오는 행과 열의 크기가 같을테니까 임의의 하나의 행렬의 길이 넣기, arr1 선택
        x = []
        for l in range(len(arr1[0])): # 각각의 같은 행과 같은 열의 값을 더해야 하니까 아무거나 하나의 행렬의 길이를 선택, 임의로 arr1[0] 행렬 선택
            x.append(arr1[i][l]+arr2[i][l])
        answer.append(x)    
    return answer