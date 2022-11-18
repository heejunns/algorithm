# 내 개인적으로는 꽤 난이도가 있는것 같다. 
# 가장 중요한 이 프로그램을 만들 때 중요한것은 모든 자리의 숫자들의 8진수에서 2진수로 변환 할 때 앞에 0 이 있어도 그대로 출력 되지만 
# 가장 큰자리의 숫자의 변환에 있어 앞에 0이 있다면 잘라내고(생략)하고 사용해야 해야 한다. 그리고 지금까지의 1의 자리 숫자 말고 10의 자리 
# 100의 자리 등의 이상의 숫자들을 한번에 2진수로 변환하게 되면 개뱔로 변환 할때와 값이 다르게 나온다. 이문제는 뭘까? 이 문제를 찾아내서 
# 해결하는 것이 이 프로그램의 가장 중요한 프로그램을 만들 때 고려요소 일 것 이다. 
number = int(input()) # 일단 변환 할 8진수의 값을 입력 받는다. 문자열로 값을 받아 for 문으로 하나씩 2진수로 변환 할 생각이다. 
y = []
m = 3
for i in str(number):
    x = []
    while True: # while 문을 탈출하는 조건을 만들어야 해서 
        if len(x) == m:
            break
        if int(i) == 0 or int(i) == 1:
            x.insert(0,str(i))
            if len(x) == 3:
                y.append(x)
            elif len(x) == 2:
                x.insert(0,str(0))
                y.append(x)
            elif len(x) == 1:
                x.insert(0,str(0))
                x.insert(0,str(0))
                y.append(x)
        else:
            x.insert(0,str(int(i)%2))
            i = int(i)//2
z = 1
q = 0 
total  = ""
while z <=len(y):
    total += ("".join(y[q]))
    q+=1
    z+=1
count = 0 
h =[]
for i in total:
    if i == "0" and count == 0:
        continue
    elif i == "1" and count == 0 :
        h.append(i)
        count +=1
    elif count ==1:
        h.append(i)
print(int("".join(h)))
