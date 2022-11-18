a = input()
x = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
y = "AZYXWUTSRQPONMLKJIHGFEDCB"
h = "A"
total = 0
for i in a:
    if abs(int(x.find(i))-int(x.find(h))) >= abs(int(y.find(i))-int(y.find(h))):
        total+=abs(int(y.find(i))-int(y.find(h)))
        h = i
    else:
        total+=abs(int(x.find(i))-int(x.find(h)))
        h = i 

print(total)
        
