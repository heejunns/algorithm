n = 1
y = []
while True:
    x = []
    a = input()
    b = input()
    if a== "END" and b == "END":
        break
    for i in b:
        x.append(i)
    for l in a:
        if l in x:
            x.pop(x.index(l))
    if x == []:
        x1 = "Case"+" "+str(n)+":"+" "+"same"
        y.append(x1)
        n+=1
    else:
        x2 = "Case"+" "+str(n)+":"+" "+"different"
        y.append(x2)
        n+=1
for k in y:
    print(k)
    
