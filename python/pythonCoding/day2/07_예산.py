'''
입력
4
120 110 140 150
485

출력
127
'''
import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    needs = list(map(int, readl().split()))
    M = int(readl())
    return N, needs, M

def Check(limit):
    s = 0
    for n in needs:
        s += n if n < limit else limit
    return s <= M


def GetSolution():
    sol = -1
    s = 0
    e = max(needs)
    while s <= e:
        m = (s + e) // 2
        if Check(m):
            sol = m
            s = m + 1
        else:
            e = m - 1
    return sol



sol = -1

# 입력받는 부분
N, needs, M = input_data()

# 여기서부터 작성
sol = GetSolution()

# 출력하는 부분
print(sol)