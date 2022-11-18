n = int(input())
m = int(input())
x = str(n)
y = x[:len(x)-2]+"00"
q = 0 
while True:
    if (int(y)+q)%m == 0 :
        break
    else:
        q+=1
if len(str(q))== 1:
    print("0"+str(q))
else:
    print(q)


