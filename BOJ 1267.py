n = int(input())
x = list(map(int,input().split()))
result_y = 0
result_m = 0
# 요금제 계산하기 
for i in x:
    result_y += ((i//30)+1)*10 # 영식 요금제 
    result_m += ((i//60)+1)*15 # 민식 요금제 
if result_y < result_m:
    print("Y",result_y)
elif result_y > result_m:
    print("M",result_m)
elif result_y == result_m:
    print("Y","M",result_y)
