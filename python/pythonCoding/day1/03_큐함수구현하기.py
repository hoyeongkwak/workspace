'''
import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    A = list(map(int, readl().split()))
    return N, A


def Push(d):
    global queue, wp, rp
# 여기서부터 작성
    if wp >= 5: return 0
    queue[wp] = d
    wp += 1
    return 1

def Pop():
    global queue, wp, rp
# 여기서부터 작성
    if wp == rp: return 0
    ret = queue[rp]
    rp += 1
    return rp

def Solve():
    for i in range(N):
        if A[i] > 0:
            r = Push(A[i])
            if r == 0: print(-1, end=' ')
        else:
            r = Pop()
            if r == 0: print(-1, end=' ')
            else: print(r, end=' ')


queue = [0]*5
wp = 0
rp = 0

# 입력받는 부분
N, A = Input_Data()

# 여기서부터 작성
Solve()
'''

import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_cmd = [list(map(int,readl().split())) for _ in range(N)]
    return N, list_cmd


def Process():
    #collection사용시
    q = deque()
    for n in range(N):
        if list_cmd[n][0] == 1:
            q.append(list_cmd[n][1])
        elif list_cmd[n][0] == 0:
            if len(q) == 0:
                print("E")
            else:
                d = q.popleft()
                print(d)
        elif list_cmd[n][0] == 2:
            print(len(q))
    '''
    q = []
    for n in range(N):
        if list_cmd[n][0] == 1:
            q.append(list_cmd[n][1])
        elif list_cmd[n][0] == 0:
            if len(q) == 0:
                print("E")
            else:
                d = q.pop(0)
                print(d)
        elif list_cmd[n][0] == 2:
            print(len(q))
    '''


N, list_cmd = Input_Data()
Process()