n = int(input())
x = list(map(int,input().split()))
count = n
for i in x:
    if i == 1:
        count-=1
    elif i >2 and i%i == 0 and i %1 == 0 :
        for l in range(2,i):
            if i%l == 0 :
                count-=1
                break
print(count)
