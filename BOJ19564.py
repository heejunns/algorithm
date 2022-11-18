import string
a = input()
x = string.ascii_lowercase
y = []
count = 1
for i in a:
    z = x.find(i)
    y.append(z)

q = [y[0]]
n = 0
for i in y[1:]:
    if i > q[n]:
        n+=1
        q.append(i)
    else:
        count+=1
        n+=1
        q.append(i)
print(count)
