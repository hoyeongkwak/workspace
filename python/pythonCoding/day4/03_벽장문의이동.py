'''
입력
7
2 5
4
3
1
6
5

출력
5
'''

import sys
def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    A, B = map(int, readl().split())
    S = int(readl())
    seq = [int(readl()) for _ in range(S)]
    return N, A, B, S, seq

def DFS(s, o1, o2, sum_move):
    global sol
    if s >= S:
        if sol > sum_move:
            sol = sum_move
        return

    #o1 -> seq[s]
    DFS(s+1,seq[s], o2, sum_move + abs(o1 - seq[s]))

    #o2 -> seq[s]
    DFS(s+1, o1, seq[s], sum_move + abs(o2 - seq[s]))

sol = -1

#입력받는 부분
N, A, B, S, seq = input_data()

# 여기서부터 작성
'''
N 전체벽장갯수
A, B : 처음에 열려있는 벽장
S : 열어야되는 벽장수
seq : 연 벽장
'''
# DFS(s, o1, o2, sum_move)
sol = 999999999999
DFS(0, A, B, 0)

# 출력하는 부분
print(sol)