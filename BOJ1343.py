n = input()
x = []
count = 0 
for i in n:
    if i == "X":
        count+=1
    elif i == ".":
        if count%2 == 1:
            x.append(count)
            x.append(0)
            count = 0 
        elif count != 0 :
            x.append(count)
            x.append(0)
            count = 0 
        elif count == 0 :
            x.append(0)
if count !=0 :
    x.append(count)
y = ""
count = 0 
for l in x:
    if l%2 == 1:
        print(-1)
        break
    else:
        if l == 0 :
            y+="."
        if l//4 != 0 :
            y+=("A"*(l//4)*4)
        if (l%4)//2 !=0:
            y+=("B"*((l%4)//2)*2)
        count+=1
        if count == len(x):
            print(y)
    
   

