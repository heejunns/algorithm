# 프로그래머스 K번째수 (level 1)
def solution(array, commands):
    answer = []
    for i in commands:
        x = array[i[0]-1:i[1]] # 주어지는 인자가 몇번째니까 인덱스로는 -1 해야한다. 마지막 인덱스는 포함하지 않으니까 -1 할 필요 없다.
        x.sort() 
        answer.append(x[i[2]-1])
        x = []
    return answer