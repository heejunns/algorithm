n = input() # 같은 숫자가 붙어있는 것을 카운트 적은 카운트를 뒤집기 
count0 = 0
count1 = 0  
m = 0
for i in n[1:]:
    if n[m]==i:
        m+=1
        continue
    elif n[m]!=i:
        if n[m] == "0":
            count0 +=1
        elif n[m] == "1":
            count1+=1
        m+=1
if n[len(n)-1] =="0":
    count0+=1
elif n[len(n)-1] == "1":
    count1+=1

if count0>=count1:
    print(count1)
else:
    print(count0)
