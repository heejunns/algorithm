# 백준 17608 번 막대기
import sys
n = int(sys.stdin.readline()) # 입력받을 막대기 개수
total = [] # 총 입력 받은 막대기의 높이를 저장할 리스트
max_height = 0 # 가장 높은 막대기의 높이를 저장할 변수
count = 0 # 오른쪽에서 볼때 보이는 막대기의 개수
for i in range(n):
    inputs = int(sys.stdin.readline())
    total.append(inputs)


for i in range(len(total)):
      if max_height < total[-1]: # max_height 보다 크다면 보이는 것이니까 
        max_height = total.pop() # max_height 에 값을 저장
        count+=1 # 보이는 막대기의 개수 +1 
      else:
        total.pop() # max_height 보다 같거나 작다면 안보일테니까 그냥 꺼내기
 
print(count) # 총 보이는 막대기 개수

