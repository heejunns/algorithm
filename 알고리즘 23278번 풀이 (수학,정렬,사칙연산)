a,b,c = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
if b == 0 and c == 0:
    print(sum(x)/len(x))
elif b ==0 and c!=0:
    print(sum(x[:(len(x)-1)-(c-1)])/(len(x)-c))
elif b!=0 and c ==0 :
    print(sum(x[b:])/(len(x)-b))
else:
    print(sum(x[b:(len(x)-1)-(c-1)])/(len(x)-c-b))

    
