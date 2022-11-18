n = int(input())
a = 1 
x = []
while a <= n:
    result = list(map(int,input().split()))
    if result[0] == result[1] == result[2]:
        total = 10000+(result[0]*1000)
        x.append(total)
        a+=1
    elif result[0]== result[1]:
        total = 1000 + (result[0]*100)
        x.append(total)
        a+=1
    elif result[0] ==result[2]:
        total = 1000 + (result[0]*100)
        x.append(total)
        a+=1
    elif result[1]==result[2]:
        total = 1000 + (result[1]*100)
        x.append(total)
        a+=1
    else:
        m = max(result)
        total = m*100
        x.append(total)
        a+=1

print(max(x))
