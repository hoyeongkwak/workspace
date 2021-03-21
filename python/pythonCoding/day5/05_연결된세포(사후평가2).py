'''
입력
4
4
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0

출력
5
'''

import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    M = int(readl())
    N = int(readl())
    map_cell = [list(map(int, readl().split())) for _ in range(M)]
    return M, N, map_cell
'''
def Flood_Fill(r,c):
    d = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    q = deque()
    q.append((r,c))
    map_cell[r][c] = 0
    cnt=1
    while q:
        r,c = q.popleft()
        for dr,dc in d:
            nr,nc = r+dr,c+dc
            if not 0<=nr<M: continue
            if not 0<=nc<N: continue
            if map_cell[nr][nc] == 0:continue
            map_cell[nr][nc] = 0
            q.append((nr,nc))
            cnt+=1
    return cnt
 
 
def Get_Solution():
    max_size = 0
    for r in range(M):
        for c in range(N):
            if map_cell[r][c]:
                size = Flood_Fill(r,c)
                if max_size < size:
                    max_size = size
    return max_size

'''
def Flood_Fill(r,c):
    d = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1))
    q = deque()
    q.append((r,c))
    map_cell[r][c] = 0
    cnt = 1
    while q:
        r,c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if not 0 <= nr < M: continue
            if not 0 <= nc < N: continue
            if map_cell[nr][nc] == 0: continue
            map_cell[nr][nc] = 0
            q.append((nr,nc))
            cnt += 1
    return cnt

def GetSolution():
    maxSize = 0
    list_size = []
    for r in range(M):
        for c in range(N):
            if map_cell[r][c]:
                size = Flood_Fill(r,c)
                '''
                if size > maxSize:
                    maxSize = size
                '''
                list_size.append(size)
    list_size.sort(key=lambda x:-x)
    maxSize = list_size[0]
    return maxSize

sol = -1
#입력 받는 부분
M, N, map_cell = Input_Data()

#여기서부터 작성
sol = GetSolution()
'''
M : 행의 크기
N : 열의 크기
map_cell : 행렬의 세포들의 값

가장 큰 구역의 세포 1의 개수 출력
'''

#출력하는 부분
print(sol)