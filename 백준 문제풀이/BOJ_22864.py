# 백준 22864번, 피로도
import sys
a,b,c,m = map(int,sys.stdin.readline().rstrip().split()) # a,b,c,m 입력받기
my_fatigue = 0 # 피로도
my_work = 0 # 일한 양 
time = 0 # 시간 
if a <= m: # 
    while time < 24: # time 이 24보다 작다면 반복
        if my_fatigue + a <= m: # 현재 피로도 + 일했을때의 피로도 a 가 피로도 한계 m 보다 작거나 같다면
            my_fatigue+=a # 피로도 상승
            my_work+=b # 일한 양 상승
            time+=1 # 시간 상승
        else:
            if my_fatigue-c >= 0: # 현재 피로도에서 쉬었을때 줄어드는 피로도 c 를 빼었을때 0 보다 크거나 같다면
                my_fatigue-=c # 피로도 감소
                time+=1 # 시간 상승
            else: # 현재 피로도에서 쉬었을때 줄어드는 피로도 c 를 빼었을때 음수라면
                my_fatigue = 0 # 피로도 0 으로 초기화
                time+=1 # 시간 상승
print(my_work)

