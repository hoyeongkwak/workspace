import sys

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int,readl().split())
    return N, M

flag = [0] * (7)
num = [0] * (5)

def Dice1(n):
    if n >= N:
        print(*num[:N])
        return
    for i in range(1, 7):
        num[n] = i
        Dice1(n+1)

def Dice2(n, s):
    if n >= N:
        print(*num[:N])
        return
    for i in range(s, 7):
        num[n] = i
        Dice2(n+1, i)


def Dice3(n):
    if n >= N:
        print(*num[:N])
        return
    for i in range(1, 7):
        if flag[i]: continue
        num[n] = i
        flag[i] = 1
        Dice3(n+1)
        flag[i] = 0


# 입력받는 부분
N, M = Input_Data()

# 여기서부터 작성
if M == 1: Dice1(0)
elif M == 2: Dice2(0,1)
elif M == 3: Dice3(0)