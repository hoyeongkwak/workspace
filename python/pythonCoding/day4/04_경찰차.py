'''
입력
6
3
3 5
5 5
2 3

출력
9
'''
'''
import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    W = int(readl())
    pos = [list(map(int,readl().split())) for n in range(W)]
    return N, W, pos
def DFS(s, p1, p2, sum_move):
    global sol
    if sum_move >= sol: return
    if s >= W:
        if sol > sum_move:
            sol = sum_move
        return
    DFS(s+1, s, p2, sum_move + abs(p1[0] - pos[s][0]) + abs(p1[1] - pos[s][1]))
    DFS(s+1, p1, s, sum_move + abs(p2[0] - pos[s][0]) + abs(p2[1] - pos[s][1]))

sol = -1
# 입력받는 부분
N, W, pos = Input_Data()

# 여기서부터 작성
sol = 99999999
DFS(0, (1,1) , (N,N) , 0)
'''

'''
N : 도로크기
W : 사건수
pos : 사건위치
경찰차의 총 이동거리

W 첫,                                    두
W+1, (W번 사건위치), 그대로 + summove    W+1, 그대로, W번 사건위치 + summove
'''

# 출력하는 부분
#print(sol)


import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    W = int(readl())
    pos = [list(map(int,readl().split())) for n in range(W)]
    return N, W, pos

def DFS(w,p1,p2,sum_dist):
    global sol
    if sum_dist >= sol: return
    if w>=W:
        sol = sum_dist
        return

    DFS(w+1,w,p2,sum_dist+abs(pos[p1][0]-pos[w][0])+abs(pos[p1][1]-pos[w][1]))
    DFS(w+1,p1,w,sum_dist+abs(pos[p2][0]-pos[w][0])+abs(pos[p2][1]-pos[w][1]))

sol = -1
# 입력받는 부분
N, W, pos = Input_Data()

# 여기서부터 작성
pos.append([1,1])
pos.append([N,N])
sol = 99999999
DFS(0, W, W+1, 0)

# 출력하는 부분
print(sol)
