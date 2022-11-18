# BOJ 22864 피로도 
a,b,c,d = map(int,input().split())
time = 0
total = 0 
result = 0 
while time <=24:
    if d//a == 0:
        break
    elif d//a > 0:
        if time + (d//a) > 24:
            time+=(d//a) # 시간
            print("현재 시간",time)
            result += (d//a)*b # 일 양 
            print("현재 일의 양",result)
            total+= (d//a) * a # 피로도 양 
            print("현재 피로도 양",total)
            time += ((d//a)*a)//c
            print("현재 시간",time)
            total -= (((d//a)*a)//c)*c
            print("햔재 피로도",total)
            print("한 턴")
print(result)