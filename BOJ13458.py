a = int(input())
x = list(map(int,input().split()))
b,c = map(int,input().split())
count = 0 
for i in x:
    if i <= b:
        count+=1
    elif i>b:
        result = (i-b)
        count+=1
        if (result%c) == 0:
            count+=(result//c)
        else:
            count+=((result//c)+1)
print(count)
