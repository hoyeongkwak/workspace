'''
입력
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

출력
8
'''
import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    C, R = map(int,readl().split())
    map_box = [[0]*(C+2) if (r==0 or r==R+1) else [0]+list(map(int,readl().split()))+[0] for r in range(R+2)]
    return C,R,map_box

def Init_BFS(q):
    #(r, c, time)
    cnt_tomato = 0
    for r in range(1, R+1):
        for c in range(1, C+1):
            if map_box[r][c] == 1:
                q.append((r, c, 0))
            elif map_box[r][c] == 0:
                cnt_tomato += 1
    return cnt_tomato

def BFS():
    d = [(0,-1),(0,1),(-1,0),(1,0)]
    q = deque()
    cnt_tomato = Init_BFS(q)
    if cnt_tomato == 0: return 0

    while len(q) > 0:
        r, c, time = q.popleft()
        for dr, dc in d:
            nr, nc, ntime = r + dr, c + dc, time + 1
            if not (1 <= nr <= R): continue
            if not (1 <= nc <= C): continue
            if map_box[nr][nc] != 0: continue

            cnt_tomato -= 1
            if cnt_tomato == 0: return ntime

            q.append((nr, nc, ntime))
            map_box[nr][nc] = 1
    return -1

'''
def BFS():
    q = deque()
    d = ((-1,0), (1,0), (0,-1),(0,1))
    cnt = 0
    for n in range(len(map_box)):
        for m in range(len(map_box[0])):
            if map_box[n][m] == 1:
                q.append((m,n))
    print(q)
    while q:
        c, r = q.popleft()
        for dc, dr in d:
            nc, nr = c + dc, r + dr
            if not (1<=nr<=R): continue
            if not (1<=nc<=C): continue
            if map_box[nc][nr] == 1: continue
            if map_box[nc][nr] == 0:
                if nr == R and nc == C: return cnt
                map_box[nc][nr] = 1
                cnt += 1
                q.append((nr, nc))
    return -1
'''
sol = -2

# 입력받는 부분
C,R,map_box = Input_Data()

# 작성하는 부분
sol = BFS()


# 출력하는 부분
print(sol)