'''
입력
5 5
0 2 2 5 9
2 0 3 4 8
2 3 0 7 6
5 4 7 0 5
9 5 6 5 0

출력
8
1 3 5
'''
import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int,readl().split())
    matrix = [[0] * (N+1) if n == 0 else [0]+list(map(int,readl().split())) for n in range(N+1)]
    return N, M, matrix

def Make_Path(path, prev, no):
    if no == 0: return
    Make_Path(path, prev, prev[no])
    path.append(no)

def BFS():
    # 각 상태의 최고 경험! : chk[]
    path = []
    prev = [0] * (N+1)
    chk = [9999999999] * (N+1)
    #(역, 시간)
    q = deque()
    q.append((1, 0))
    chk[1] = 0

    while len(q)>0:
        no, time = q.popleft()
        for n_no in range(1, N+1):
            ntime = chk[no] + matrix[no][n_no]
            if chk[n_no] <= ntime: continue
            prev[n_no] = no
            chk[n_no] = ntime
            q.append((n_no, ntime))

    Make_Path(path, prev, M)

    return chk[M], path

#입력받는 부분
N, M, matrix = Input_Data()

#N 전체역, M 도착지
# 여기서부터 작성
sol, path = BFS()

print(sol)
print(*path)
