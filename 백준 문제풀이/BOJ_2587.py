# 백준 2587번 대표값2
import sys
total = []
sum = 0
for i in range(5):
    n = int(sys.stdin.readline())
    sum+=n
    total.append(n)
total.sort()
print(int(sum/5))
print(total[2])