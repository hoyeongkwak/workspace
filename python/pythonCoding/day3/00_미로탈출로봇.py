'''
입력
8 7
1 2 7 5
11111111
00000111
10110011
10111001
10111101
10000001
11111111

출력
9
'''
'''
상태 : 로봇위치, 시간(초)
상태발전 : 1칸이동행동(위치변경, 시간 + 1
최종상태 : 도착위치


R = 0 111111111111111111 벽


R + 1 111111111111111111 벽
'''

import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    C, R = map(int,readl().split())
    sc,sr,ec,er = map(int,readl().split())
    map_maze = [[1]*(C+2)if (r == 0 or r == R+1) else [1] +list(map(int,readl().strip()))+[1] for r in range(R+2)]
    return C,R,sc,sr,ec,er,map_maze

def BFS():
    q = deque()
    chk = [[0]*(C+2) for r in range(R+2)]
    #상태 : (행, 열, 시간)
    #초기 상태 정의
    q.append((sr,sc,0))
    chk[sr][sc] = 1
    while len(q) > 0:
        r, c, time = q.popleft()
        #상태 발전 : 위치 상하좌우 이동, 시간 + 1
        for dr, dc in ((-1,0), (1,0), (0,-1),(0,1)):
            nr, nc, nTime = r + dr, c + dc, time + 1
            if not (1<=nr<=R): continue
            if not (1<=nc<=C): continue
            if map_maze[nr][nc] == 1: continue
            if chk[nr][nc] == 1: continue  #map_maze를 망치지 않고 유지해야 할 때

            if nr == er and nc == ec: return nTime

            q.append((nr,nc,nTime))
            chk[nr][nc] = 1
            #map_maze[nr][nc] = 1
    return -1


sol = -1
#입력받는 부분
C,R,sc,sr,ec,er,map_maze = Input_Data()

#여기서부터 작성
sol = BFS()

#출력하는 부분
print(sol)