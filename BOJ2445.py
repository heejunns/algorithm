n = int(input())
x = 0
y = 1
z = []
q = 1
while y <= (2*n):
    z.append(" ")
    y+=1
while n>0:
    z[x] = "*"
    z[(len(z))-q] = "*"
    x+=1
    q+=1
    n-=1
    print("".join(z))
x-=1
q-=1
while n< (len(z)/2):
   n+=1
   z[x] = " "
   z[len(z)-q] = " "
   q-=1
   x-=1
   print("".join(z))
