n = int(input())
m = int(input())
x = []
if n >= 5:
    x.append(m-500)
if n >= 10:
    x.append(m-((m//100)*10))
if n >= 15:
    x.append(m-2000)
if n >= 20:
    x.append(m-((m//100)*25))

if x == []:
    print(m)
elif min(x) < 0 :
    print(0)
else:
    print(min(x))
