# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    info_filter = [list(map(int,  readl().split())) for _ in range(N)]
    return N,  info_filter


def solve_bin(n,  cnt,  ref,  tr):
    global sol_diff, sol_cnt

    if n>=N:
        if cnt>0 and (sol_diff > abs(ref-tr) or (sol_diff == abs(ref-tr) and cnt < sol_cnt)):
            sol_diff = abs(ref-tr)
            sol_cnt = cnt
        return

    solve_bin(n+1,  cnt,  ref,  tr)
    solve_bin(n+1,  cnt+1,  ref*info_filter[n][0],  tr+info_filter[n][1])

def solve_multi(s,  cnt,  ref,  tr):
    global sol_diff, sol_cnt
    if cnt>0 and (sol_diff > abs(ref-tr) or (sol_diff == abs(ref-tr) and cnt < sol_cnt)):
        sol_diff = abs(ref-tr)
        sol_cnt = cnt

    for i in range(s,  N):
        solve_multi(i+1,  cnt+1,  ref*info_filter[i][0],  tr+info_filter[i][1])

sol = -1
# 입력받는 부분
N,  info_filter = input_data()

# 여기서부터 작성
sol_diff = 2**60-1
sol_cnt = 1

solve_bin(0,  0,  1,  0)
#solve_multi(0,  0,  1,  0)
sol = N - sol_cnt

# 출력하는 부분
print(sol)

'''
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    info_filter = [list(map(int, readl().split())) for _ in range(N)]
    return N, info_filter


def DFS(n, s, r, cnt):
	if n >= N-1:
		return cnt
	if abs(s - r) < abs((s * info_filter[n+1][0]) - (r + info_filter[n+1][1])): cnt += 1
	DFS(n+1, s * info_filter[n+1][0], r + info_filter[n+1][1], cnt)

sol = -1
# 입력받는 부분
N, info_filter = input_data()

# 여기서부터 작성
sol = DFS(0,1,0,0)

# 출력하는 부분
print(sol)
'''