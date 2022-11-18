n = int(input())
x = 1
count = 0 
while x <= n:
    z = "s"
    y = []   
    a = input()
    for i in a:
        if i in y and i == z: # i 가 y 에 있고 i 가 y의 전 원소랑 같다면 
            z = ""
            z+=i
        elif i in y and i !=z: # i 가 y에 있고 i 가 y의 전 원소랑 다르다면 
            y.clear()
            break
        elif i not in y: # i 가 y에 있지 않으면 
            y.append(i)
            z = ""
            z +=i
    if y != []:
        count+=1 
    x+=1
print(count)
