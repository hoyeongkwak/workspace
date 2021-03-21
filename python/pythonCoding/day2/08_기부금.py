import sys

def input_data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    insentive = list(map(int, readl().split()))
    return N, M, insentive


def Check(limit):
    # return sum([0 if money <= limit else (money - limit) for money in insertive]) >= M
    s = 0
    for n in insentive:
        if n >= limit:
            s += (n - limit)
            if s >= M: return True
    return False

def GetSolution():
    sol = -1
    s = 0
    e = max(insentive)
    while s <= e:
        m = (s + e) // 2
        if Check(m):
            sol = m
            s = m + 1
        else:
            e = m -1
    return sol


sol = -1

# 입력받는 부분
N, M, insentive = input_data()

# 여기서부터 작성
sol = GetSolution()

# 출력하는 부분
print(sol)