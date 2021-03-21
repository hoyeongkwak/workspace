'''
입력
5 6
0 0 0 0 0 0
0 1 1 0 1 0
0 1 0 0 0 0
0 0 1 1 1 0
1 0 0 0 0 0
4 2 3
2 4 1

출력
9
'''
import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    R, C = map(int, readl().split())
    map_factory = [[1]+list(map(int, readl().split()))+[1] if 1<=r<=R else [1]*(C+2) for r in range(R+2)]
    status_s = list(map(int,readl().split())) #행, 열, 방향 (동서남북, 1234)
    status_e = list(map(int,readl().split()))
    return R, C, map_factory, status_s, status_e

def BFS():
    d = ((-1, 0),(0,1),(1,0),(0,-1))
    q = deque()
    lut_dir = [0,1,3,2,0] # lut_dir[원래방향]
    status_s[2] = lut_dir[status_s[2]]
    status_e[2] = lut_dir[status_e[2]]
    chk = [[[0]*(C+2) for r in range(R+2)] for _ in range(4)]   # chk[dir][r][c]

    q.append((*status_s,0)) #(행,열,방향,명령사용수)
    chk[status_s[2]][status_s[0]][status_s[1]] = 1

    while q:
        r,c,dir,cnt = q.popleft()

        for k in range(1,4):
            nr,nc,ndir,ncnt = r + (k*d[dir][0]),c + (k*d[dir][1]),dir,cnt+1
            if map_factory[nr][nc] == 1: break
            if chk[ndir][nr][nc] == 1: continue
            if [nr,nc,ndir] == status_e: return ncnt
            q.append((nr,nc,ndir,ncnt))
            chk[ndir][nr][nc] = 1

        for t in range(2): # 0-left 1-right
            nr,nc,ndir,ncnt = r,c, (dir + [3,1][t])%4 ,cnt+1
            if chk[ndir][nr][nc] == 1: continue
            if [nr,nc,ndir] == status_e: return ncnt
            q.append((nr,nc,ndir,ncnt))
            chk[ndir][nr][nc] = 1

    return -1



sol = -1
# 입력받는 부분
R, C, map_factory, status_s, status_e = input_data()

# 여기서부터 작성
'''
R, C = 세로, 가로 길이
map_factory : 공장지도
status_s 로봇의 시작점과 방향
status_e 로봇이 최종도착점과 방향
상태: r,c, dir     명령사용수 
상태발전 : 명령1번을 이용해서 제어
r,c, dir, cnt_cmd

r + dr, c + dc ->해당방향

     4
   2   1
     3
'''
sol = BFS()
# 출력하는 부분

print(sol)