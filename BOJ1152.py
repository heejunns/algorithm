# BOJ 1152 단어의 개수 
s = input().strip()
count = 0 # 공백의 개수를 세기 위한 변수 
test = 0 # 혹시 아무 문자열도 입력되지 않고 공백만 입력될 경우를 대비해 공백이 아니라면 기록하기 위한 변수   
for i in s:
    if i == " ":
        count+=1 # 공백의 개수 세기 
    if i != " ":
        test+=1
if test > 0: # test가 0이 아니고 1이라도 증가하면 문자가 있다는 뜻이기 때문에 
    print(count+1) # 공백의 개수에서 +1 출력 
elif test == 0 :
    print(0)


