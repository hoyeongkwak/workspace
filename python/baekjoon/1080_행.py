import sys
readl = sys.stdin.readline

N, M = readl().split()
N = int(N)
M = int(M)
nList = []

for i in range(N*2):
    nList.append(list(map(int, readl().split())))

print(nList)