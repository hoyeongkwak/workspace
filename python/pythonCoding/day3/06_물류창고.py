# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque


def input_data():
    readl = sys.stdin.readline
    N,  M = map(int, readl().split())
    infos = [list(map(int,  readl().split())) for _ in range(M)]
    return N,  M,  infos


def make_matrix():
    mat = [[0x7fffffff]*(N+1) for _ in range(N+1)]
    for a, b, d in infos:
        mat[a][b] = mat[b][a] = d
    return mat


def bfs(s):
    q = deque()
    q.append((s,  0))
    chk = [0x7fffffff] * (N+1)
    chk[s] = 0

    while q:
        n,  dist = q.popleft()
        if chk[n] != dist: continue
        for nn in range(1,  N+1):
            if mat[n][nn] == 0x7fffffff: continue
            if chk[nn] <= chk[n] + mat[n][nn]: continue
            chk[nn] = chk[n] + mat[n][nn]
            q.append((nn, chk[nn]))

    return max(chk[1:])


def solve():
    sol = 0x7fffffff
    for s in range(1, N+1):
        t = bfs(s)
        sol = min(t,  sol)
    return sol


# 입력받는 부분
N,  M,  infos = input_data()

# 여기서부터 작성
mat = make_matrix()

sol = solve()

# 출력하는 부분
print(sol)