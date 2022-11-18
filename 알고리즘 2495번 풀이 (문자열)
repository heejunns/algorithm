n1 = input()
n2 = input()
n3 = input()
x = [n1,n2,n3]
y = []
for i in x:
    count = 0
    result = ""
    q = []
    for l in i:
        if result =="":
            result+=l
            count+=1
        elif result == l:
            count+=1
            result = ""
            result+=l
        else:
            q.append(count)
            result = ""
            result+=l
            count = 1
    q.append(count)
    y.append(max(q))
for k in y:
    print(k)
