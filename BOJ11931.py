# BOJ 11931 수 정렬하기 4
import sys 
n = int(sys.stdin.readline())
x = []
for i in range(n):
    a = int(sys.stdin.readline())
    x.append(a)
x.sort()
x.reverse()
for i in x:
    print(i)    