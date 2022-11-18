import sys
n = int(sys.stdin.readline())
result = []
for i in range(n):
    x = ""
    y = []
    a = sys.stdin.readline().strip()
    for l in a:
        if l != " ":
            x+=l
        else:
            y.append(x)
            x = ""
    y.append(x)
    if y[1] == "+":
        if int(y[0])+int(y[2]) == int(y[4]):
            result.append("correct")
        else:
            result.append("wrong answer")
    elif y[1] == "-":
        if int(y[0])-int(y[2]) == int(y[4]):
            result.append("correct")
        else:
            result.append("wrong answer")
    elif y[1] == "*":
        if int(y[0])*int(y[2]) == int(y[4]):
            result.append("correct")
        else:
            result.append("wrong answer")
    elif y[1] == "/":
        if int(y[0])/int(y[2]) == int(y[4]):
            result.append("correct")
        else:
            result.append("wrong answer")
for k in result:
    print(k)
