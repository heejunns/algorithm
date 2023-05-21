# 백준 2178번, 미로탐색
import sys
from collections import queue
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(info,a,b):
