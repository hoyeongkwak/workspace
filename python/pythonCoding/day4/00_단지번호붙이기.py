import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_apt = [[0] + list(map(int,list(readl().strip()))) + [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
    return N, map_apt
def Flood_Fill(r,c):
    d = ((1,0),(-1,0),(0,1),(0,-1))
    q = deque()
    q.append((r,c))
    map_apt[r][c] = 0
    cnt = 1
    while q:
        r,c = q.popleft()
        for dr,dc in d:
            nr,nc = r+dr,c+dc
            if map_apt[nr][nc] == 0: continue
            map_apt[nr][nc] = 0
            q.append((nr,nc))
            cnt+=1
    return cnt


def Get_Solution():
    list_size = []
    for r in range(1,N+1):
        for c in range(1,N+1):
            if map_apt[r][c]:
                size = Flood_Fill(r,c)
                list_size.append(size)
    list_size.sort()
    return len(list_size), list_size

# 입력받는 부분
N, map_apt = Input_Data()

# 여기서부터 작성
cnt,list_size = Get_Solution()

# 출력하는 부분
print(cnt)
print(*list_size,sep='\n')