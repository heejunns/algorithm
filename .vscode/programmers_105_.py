# 프로그래머스 직사각형 별찍기 (level 1)
a, b = map(int, input().strip().split(' '))
for i in range(b):
    for l in range(a):
        print("*",end = "")
    print()