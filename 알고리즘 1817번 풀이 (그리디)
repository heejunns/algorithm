a,b = map(int,input().split())
if a !=0:
    x = list(map(int,input().split()))
    count = 0
    total = 0 
    for i in x:
        if i+total <b:
          total+=i
        elif i+total == b:
           count+=1
           total = 0 
        elif i+total > b:
           count+=1
           total =0 
           total +=i
    if total !=0:
       count +=1
    print(count)
elif a == 0:
    print(0)
