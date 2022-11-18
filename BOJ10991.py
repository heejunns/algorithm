n = int(input())
x = 0 
y = []
z = 1
h = 1
q = 1
while x <n+(n-1):
    y.append(" ")
    x+=1
x = 0 

while z <=n:
    if z == 1:
        y[len(y)//2] = "*"
        print("".join(y[:((len(y)//2)+1)]))
        z+=1
        y.clear()
        while x <n+(n-1):
            y.append(" ")
            x+=1
        x = 0 
    else: 
        y[(len(y)//2) + h ] = "*"
        h -=2
        while q <z: # z는 그 줄에 들어가야할 별의 개수 
            y[(len(y)//2)+h] = "*"
            q +=1
            h -=2 
        else:
            q-=1
            h+=2
            h +=((q+1)*2)
            h-=1
            print("".join((y[:((len(y)//2)+h)])))
            h =1
            h+=(z-1)
            z+=1
            q = 1
            y.clear()
            while x <n+(n-1):
                y.append(" ")
                x+=1
            x = 0 
