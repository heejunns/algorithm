y = []
while True:
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0 :
        break
    x = c//b*a
    if c%b <a:
        x+=(c%b)
    elif c%b >=a:
        x+=a
    y.append(x)
    x = 0 
n = 1
for i in y:
    print("Case %d:"%n,i)
    n+=1



