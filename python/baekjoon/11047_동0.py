import sys

readl = sys.stdin.readline

N, K = readl().split()
N = int(N)
K = int(K)
coinList = []
cnt = 0
for i in range(N):
    c = int(readl().strip())
    coinList.append(c)
for i in range(N,0,-1):
    c = coinList[i-1]
    if K // c != 0:
        cnt = cnt + (K // c)
        K = K % c
        if K == 0:
            break
print(cnt)