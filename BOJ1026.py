# BOJ 1026 보물 
n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
x.sort()
y.sort()
y.reverse()
sum = 0 
for i in range(len(x)):
    sum+= x[i]*y[i]
print(sum)
