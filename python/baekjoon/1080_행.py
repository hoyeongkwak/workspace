import sys
readl = sys.stdin.readline

N, M = map(int, readl().split())
change_maps = [list(map(int, readl().strip())) for _ in range(N)]
result_maps = [list(map(int, readl().strip())) for _ in range(N)]
count = 0

def convert(x, y, arr):
    for i in range(x, x+3):
        for j in range(y, y+3):
            change_maps[i][j] = 1- change_maps[i][j]

for i in range(N-2):
    for j in range(M-2):
        if change_maps[i][j] != result_maps[i][j]:
            convert(i, j, change_maps)
            count += 1

ret = False
for i in range(N):
    for j in range(M):
        if change_maps[i][j] != result_maps[i][j]:
            ret = True

if ret:
    print(-1)
else:
    print(count)
