n = int(input())
x = [2]
m = 2
for i in range(29):
    m*=2
    x.append(m)
if n in  x:
    print(1)
else:
    print(0)
print(2**30)