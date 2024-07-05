import sys
from typing import List

N: int = int(input())
count: int = 0
paper:List[List[str]] = [[0 for _ in range(100)] for _ in range(100)]
for i in range(N):
    width, length = map(int, sys.stdin.readline().split())
    for x in range(width, min(width + 10, 100)):
        for y in range(length, min(length + 10, 100)):
            paper[x][y] = 1
for i in range(100):
    count += paper[i].count(1)
print(count)