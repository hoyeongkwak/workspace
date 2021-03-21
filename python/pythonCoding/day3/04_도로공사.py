import sys
from collections import deque


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    map_cost = [[0] + list(map(int,  readl()[:-1])) + [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
    return N,  map_cost


def solve():
    chk = [[0]+([99999999]*N)+[0] if 1<=r<=N else [0]*(N+2)for r in range(N+2)]
    d = ((-1,  0),  (1,  0),  (0,  -1),  (0,  1))
    q = deque()
    q.append((1,  1))
    chk[1][1] = map_cost[1][1]
    while q:
        r,  c = q.popleft()
        for dr,  dc in d:
            nr,  nc = r + dr,  c + dc
            if chk[nr][nc] > chk[r][c] + map_cost[nr][nc]:
                chk[nr][nc] = chk[r][c] + map_cost[nr][nc]
                q.append((nr,  nc))
    return chk[N][N]


sol = -2

# 입력받는 부분
N,  map_cost = input_data()

# 여기서부터 작성
sol = solve()

# 출력하는 부분
print(sol)