# BOJ 5789 한다 안한다
n = int(input())
x = []
for i in range(n):
    a = input()
    if a[(len(a)//2)-1] == a[len(a)//2]:
        x.append("Do-it")
    elif a[(len(a)//2)-1] != a[len(a)//2]:
        x.append("Do-it-Not")
for k in x:
    print(k)