# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    R, C = map(int, readl().split())
    map_park = [['X']+list(readl()[:-1])+['X'] if 1<=r<=R else ['X']*(C+2) for r in range(R+2)]
    return R, C, map_park

def GetSolution():
    q = deque()
    chk = [[0] *(C+2) for _ in range(R+2)]
    d = ((-1,0), (1,0), (0, -1), (0,1))

    q.append((1,1))
    map_park[1][1] = 'X'

    while q:
        r, c = q.popleft()

        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if map_park[nr][nc] == '.':
                if nr == R and nc == C: return chk[r][c] +1
                map_park[nr][nc] = 'X'
                #chk[r][c] -> r,c 이동하는데 걸린 시간 <- 잘 이해해두길
                chk[nr][nc] = chk[r][c] + 1
                q.append((nr, nc))
    return -1


'''
R : H, C : W
map_park : 지도
X = 공원(진입불)
도착위치 : (R-1, C-1)
'''


sol = -1

# 입력받는 부분
R, C, map_park = input_data()

# 여기서부터 입력
sol = GetSolution()
# 출력하는 부분
print(sol)