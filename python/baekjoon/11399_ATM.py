import sys

readl = sys.stdin.readline
N = int(readl().strip())

lst = list(map(int, readl().split()))
lst.sort()
wTime = 0
for i in range(N):
    wait = 0
    for j in range(i+1):
        wait = wait + lst[j]
    wTime = wTime + wait
print(wTime)