'''
입력
3
1 0
2 21
4 0

출력
6
'''
import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info

def check(adopt):
    c = 0
    for i in range(N-1):
        if info[i][1] + c >= adopt:
            c = (info[i][1] + c) - adopt - (info[i+1][0] - info[i][0])
            if c<0: c = 0
        else:
            c = -(adopt - (info[i][1] + c) + (info[i+1][0] - info[i][0]))
    return info[N-1][1] + c >= adopt

def get_solution():
    s = 0
    e = 1000000000 #최대입양가능수, 각 마을 물고기 양의 최대값으로 하는것도 방법임

    while s<=e:
        m = (s+e)//2
        if check(m):
            sol = m
            s = m + 1
        else:
            e = m - 1

    return sol
sol = -1

# 입력받는 부분
N, info = input_data()

# 여기서부터 작성

sol = get_solution()
'''
20 300              오른쪽에서 115 빌림
40 400              왼쪽에 (-115 - 20) 빌려줌 = 265, 오른쪽에서 150 빌림
340 700             왼쪽에 (-150 - 300) 빌려줌 = 250, 오른쪽에서 165 빌림
360 600             왼쪽에 (-165 - 20) 빌려줌 = 415
'''


# 출력하는 부분
print(sol)