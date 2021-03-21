'''
import sys
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    A = list(map(int, readl().split()))
    return N, A


def Push(d):
    global stack, sp
    # 여기서부터 구현
    # Full?
    if sp == 0: return -1
    sp -= 1
    stack[sp] = d
    return sp

def Pop():
    global stack, sp
    # 여기서부터 구현
    # Empty?
    if sp == 4 : return -1
    ret = stack[sp]
    sp += 1
    return ret


def Solve():
    for i in range(N):
        if A[i] > 0:
            r = Push(A[i])
            if r == -1: print(-1, end=' ')
        else:
            r = Pop()
            if r == -1: print(-1, end=' ')
            else: print(r, end=' ')


stack = [0]*4
sp = 4

N, A = Input_Data()
Solve()
'''
import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_cmd = [list(map(int,readl().split())) for _ in range(N)]
    return N, list_cmd


def Process():
    stack = []
    for n in range(N):
        if list_cmd[n][0] == 1:
            stack.append(list_cmd[n][1])
        elif list_cmd[n][0] == 0:
            if len(stack) == 0:
                print("E")
            else:
                print(stack.pop(-1))
        elif list_cmd[n][0] == 2:
            print(len(stack))


N, list_cmd = Input_Data()
Process()