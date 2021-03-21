'''
입력
5 3
0 2
4 7
9 9

출력
2
'''
import sys

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int,readl().split())
    intvals = [list(map(int,readl().split())) for _ in range(M)]
    return N, M, intvals
'''
def check(d):
    idx = 0
    last = intvals[0][0]

    for _ in range(N-1):
        while idx<M and intvals[idx][1] < last+d:
            idx+=1
        if idx == M: return False
        last = intvals[idx][0] if intvals[idx][0] > last + d else last + d
    return True


def Get_Solution():
    intvals.sort()
    s,e = 0,intvals[-1][1]

    while s<=e:
        m = (s+e)//2
        if check(m):
            sol = m
            s = m+1
        else:
            e = m-1
    return sol
'''


def GetSolution():
    temp = []
    for s, e in intvals:
        for i in range(s,e+1):
            temp.append(i)
    nMin = 999999999
    prev = temp[0]
    cnt = 1

    for i in temp:
        if cnt == N:
            return nMin
        if (i - prev) >= 2:
            if (i - prev) <= nMin:
                nMin = i - prev
            prev = i
            cnt += 1
    return nMin
'''
    Last = max(intvals)[1]
    gList = [0] * (Last + 2)
    oList = [0] * N
    cnt = 0
    for s, e in intvals:
        for i in range(s,e+1):
            gList[i] = 1

    for i in range(Last + 2):
        if cnt >= N:
            break
        if gList[i] == 1:
            if cnt == 0:
                oList[cnt] = i
                cnt += 1
            if (i - oList[cnt-1]) >= 2:
                oList[cnt] = i
                cnt += 1
    nMin  = oList[N-1]

    for i in range(1, N-1):
        if oList[i] - oList[i-1] < nMin:
            nMin = oList[i] - oList[i-1]

    return nMin
'''
sol = -1
#입력받는 부분
N, M, intvals = Input_Data()

# 여기서부터 작성
sol = GetSolution()
#sol = Get_Solution()
'''
N : 소 마리수
M : 분리된 구간의 수
(a, b) : 잔디 구간
'''

# 출력하는 부분
print(sol)