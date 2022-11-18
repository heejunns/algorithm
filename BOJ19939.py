a,b = map(int,input().split())
total = 0 
for i in range(1,b+1):
   total +=i

if total > a:
   print(-1)
elif total == a:
   print(b-1)
elif total < a:
   if (a-total)%b ==0 :
      print(b-1)
   else:
      print(b)
