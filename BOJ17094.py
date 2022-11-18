n = int(input())
m = input()
x = 0 
y = 0 
for i in m:
    if i =="2":
        x+=1
    elif i == "e":
        y+=1
if x>y:
    print(2)
elif x<y:
    print("e")
elif x==y:
    print("yee")
