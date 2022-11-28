n = int(input())
if n<10:
    x = str(n)+"0" # str 
else:
    x = str(n)
y = str(int(x[0])+int(x[1]))
z = x[1]+y[len(y)-1]
count = 1
while x!=z:
    if int(z)<10:
        z = str(z)+"0"
    z1 = str(int(z[0])+int(z[1]))
    z = z[1]+z1[len(z1)-1]
    count+=1
print(count)
