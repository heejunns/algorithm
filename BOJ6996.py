n = int(input())
x = 1
y = []
while x <=n:
    total = 0 
    a,b  = map(str,input().split())
    y1 = []
    for k in b:
        y1.append(k)
    for i in a:
        if i in y1:
            total +=1
            y1.pop(y1.index(i))
        else:
            total = 0 
    if total == len(b):
        x1 = a+" "+"&"+" "+b+" "+"are"+" "+"anagrams."
        y.append(x1)
    else:
        x2 = a+" "+"&"+" "+b+" "+"are"+" "+"NOT"+" "+"anagrams."
        y.append(x2)
    x+=1
for l in y:
    print(l)
