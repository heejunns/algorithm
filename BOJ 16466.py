# BOJ 16466 콘서트 
# 1차 티켓팅된 티켓의 번호 빼고 가장 작은 숫자의 티켓을 티켓팅 하면 된다. 
# 내가 생각한 아이디어는 ticket 이라는 변수를 1로 초기화하여 1차 티켓팅된 티켓을 for 문으로 돌려 티켓이 있다면 +1 하면서 for문을 진행하는데 없다면 그것이 답이 됩니다. 
# 뒤죽박죽 입력되기 때문에 일단 리스트 형태로 받아 오름차순으로 정렬 후 진행하면 효과적일 것 같습니다. 
n = int(input())
x = list(map(int,input().split()))
x.sort()
ticket = 1
for i in x:
    if i == ticket:
        ticket+=1
    else:
        break
print(ticket)