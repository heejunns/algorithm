n = int(input())
x = []
count = 0 
for i in range(n):
   a = int(input())
   x.append(a)
if n == 1:
   print(0)
else:
   while True:
      if max(x) == x[0] and max(x[1:]) != x[0]: # x 리스트 중에 가장 큰 값이 x[0]과 같고 그 다음부터의 최고 값이 x[0]과 다를 때 
         break
      elif max(x) == x[0] and max(x[1:]) == x[0]: # x 리스트 중에 가장 큰 값이 x[0]과 같고 그 다음부터의 최고 값이 x[0]과 같은 값이 있을 때 
         x[(x[1:].index(max(x[1:])))+1] -=1
         count+=1
         x[0]+=1
      elif max(x) != x[0]: # x 리스트 중에 가장 큰 값이 x[0]과 값이 다를때 
         x[x.index(max(x))] -=1
         count+=1
         x[0]+=1
   print(count)
