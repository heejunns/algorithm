a = int(input())
n = 1
total_str = []
while a >= n:
    n +=1
    b = input()
    total_str.append(b)

for i in total_str:
    x = len(i)
    print(i[0]+i[(x-1)])
    
    
