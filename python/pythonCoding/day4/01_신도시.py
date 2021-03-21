'''
입력
4
0 0
2799
7439
0652
2172

출력
5
'''
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque

def input_data():
    N = int(input())
    sc, sr = map(int, input().split())
    map_city = [list(map(int,input(),[16]*(N))) for r in range(N)]
    return N, sc, sr, map_city

def checkList(m,n):
	for i in range(4):
		if pipe_list[m][i] & pipe_list[n][i] == 1:
			return 1
	return 0

def GetSolution():
	d = ((1,0),(-1,0),(0,1),(0,-1))
	q = deque()
	q.append((sr,sc))
	map_city[sr][sc] = 0
	cnt = 0
	while q:
		r,c = q.popleft()
		for dr, dc in d:
			nr, nc = r + dr, c + dc
			if not 0 <= nr <= N: continue
			if not 0 <= nc <= N: continue
			if checkList(map_city[r][c], map_city[nr][nc]) == 0: continue
			map_city[nr][nc] = 0
			q.append((nr, nc))
			cnt += 1

	print(cnt)
	return -1

def Get_Total_Count():
    cnt = 0
    for r in range(N):
        for c in range(N):
            if map_city[r][c] != 0:
                cnt+=1
    return cnt

def Flood_Fill(r,c):
    #상하좌우 0123
    d = ((-1,0),(1,0),(0,-1),(0,1))
    lut_ndir = [1,0,3,2]
    q = deque()
    q.append((r,c, map_city[r][c]))
    map_city[r][c] = 0
    cnt = 1

    while q:
        #현재위치 파이프 -> 다음위치 방향
        #다음위치 파이프 -> 현재위치 방향
        r, c, pipe = q.popleft()
        for dir in range(4):
            if not info_pipe[pipe][dir]: continue #현재위치 파이프가 다음방향으로 뻗어져 있는가?
            nr, nc, ndir = r + d[dir][0], c + d[dir][1], lut_ndir[dir]
            if not (0 <= nr < N): continue
            if not (0 <= nc < N): continue
            if not info_pipe[map_city[nr][nc]][ndir]: continue #다음위치 파이프가 현재위치 방향으로 뻗어져 있는가?
            cnt += 1
            q.append((nr, nc, map_city[nr][nc]))
            map_city[nr][nc] = 0
    return cnt

sol = -1
# 입력받는 부분
N, sc, sr, map_city = input_data()

# 여기서부터 작성
#상하좌우
info_pipe = [
	[False, False, False, False], #0번 파이프
	[False, False, True, True], #1번 파이프
	[True, True, False, False], #2번 파이프
	[False, True, False, True], #3번 파이프
	[False, True, True, False], #4번 파이프
	[True, False, True, False], #5번 파이프
	[True, False, False, True], #6번 파이프
	[True, True, False, True], #7번 파이프
	[False, True, True, True], #8번 파이프
	[True, True, True, False], #9번 파이프
	[True, False, True, True], #A번 파이프
	[True, True, True, True] #B번 파이프
]
total_cnt = Get_Total_Count()

flow_cnt = Flood_Fill(sr, sc)
sol = total_cnt - flow_cnt
'''
pipe_list = [
    (0,0,0,0),(0,0,1,1),(1,1,0,0),(0,1,0,1),
    (0,1,1,0),(1,0,1,0),(1,0,0,1),(1,1,0,1),
    (0,1,1,1),(1,1,1,0),(1,0,1,1),(1,1,1,1)
]
'''
#sol = GetSolution()
# 출력하는 부분
print(sol)