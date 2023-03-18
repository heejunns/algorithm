# 백준 26069 번 , 붙임성 좋은 총총이
import sys
n = int(sys.stdin.readline())
dance_count = 1
remember = {}
for i in range(n):
    a,b = map(str,sys.stdin.readline().rstrip().split())
    if (a == "ChongChong" or b == "ChongChong" ):
        if( a != "ChongChong" and a not in remember):
            remember[a] = 0
            dance_count+=1
        elif ( b !="ChongChong" and b not in remember  ):
            remember[b] = 0
            dance_count+=1
    elif ( a in remember or b in remember):
          if( a not in remember):
               remember[a] = 0
               dance_count+=1
          elif (b not in remember):
               remember[b] = 0
               dance_count+=1

print(dance_count)
