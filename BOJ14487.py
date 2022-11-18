n = int(input())
member = list(map(int,input().split()))
x = member.index(max(member))
member.pop(x)
total = 0 
for i in member:
    total +=i
print(total)
