n = int(input())
x = 1 
y =[]
h = 1
q = 0 
while x <= (n+(n-1)) :
    z = " "
    y.append(z)
    x+=1 
x = 1
while x <=n:
    if x == 1 and n == 1:
        y[0] = "*"
        print(y[0])
        x+=1
    else:
        if x == 1:
            y[len(y)//2] = "*"
            print("".join(y[:((len(y)//2)+1)]))
            y[len(y)//2] = " "
            x+=1
        elif x!=1 and x <=n:
            y[(len(y)//2)+h] = "*"
            y[(len(y)//2)-h] = "*"
            print("".join(y[:((len(y)//2)+h)+1]))
            y[(len(y)//2)+h] = " "
            y[(len(y)//2)-h] = " "
            h+=1
            x+=1



