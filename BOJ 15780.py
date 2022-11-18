# BOJ 15780 멀티탭 충분하니?
# 멀티탭 구의 개수에 따라서 최대 몇개의 코드를 꽂아야할지 알아야 한다. 멀티탭의 구의 개수 나누기 2를 해서 나머지가 있다면 몫에 +1을 해준 값을 꽂으면 되고 나머지가 없다면 몫의 값만 꽂는 형식의 코드를 작성한다. 
n,k = map(int,input().split())
x = list(map(int,input().split()))
t = 0
for i in x:
    if i%2 > 0:
        n-= (i//2)+1
    elif i%2 == 0:
        n-= (i//2)       
if n < 1:
    print("YES")
else:
    print("NO")

