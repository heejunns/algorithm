from collections import deque 
def solution(numbers, target): 
    answer = 0 # target과 같이 같은 경우의 수의 개수 
    k = len(numbers) # 입력되는 리스트의 길이
    index  = 0 # 인덱스 값 
    queue = deque() # deque을 이용해 queue를 만들기 
     # 첫번째 인덱스 +,- 한 이후 index와 함께 저장 
    queue.append([numbers[index],index]) 
    queue.append([-numbers[index],index])

    while queue:
        temp,index = queue.popleft() # 하나씩 꺼내기
        index+=1
        if index < k: # numbers보다 작다면 꺼내기
            queue.append([temp+numbers[index],index])
            queue.append([temp-numbers[index],index])
        elif temp == target: # 꺼낸 temp와 target이 같다면 +1
            answer+=1
    return answer

print(solution([1,1,1,1,1],3))