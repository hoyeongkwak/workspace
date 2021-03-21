'''
입력
5
3
1
10
7
4

출력
4
'''
import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = [int(readl()) for _ in range(N)]
    return N, pos

def BSLower(list_data, s, e, d):
    # rs이상 값 중 가장 작은 값
    sol = -1
    while s <= e:
        m = (s+e) // 2
        if list_data[m] >= d:
            sol = m
            e = m - 1
        else:
            s = m + 1
    return sol

def BSUpper(list_data, s, e, d):
    #re이하 값 중 최대값
    sol = -1
    while s <= e:
        m = (s+e) // 2
        if list_data[m] <= d:
            sol = m
            s = m + 1
        else:
            e = m - 1
    return sol

def GetSolution():
    cnt = 0
    pos.sort()
    for s1 in range(N):
        for s2 in range(s1+1,N):
            jump = pos[s2] - pos[s1]
            rs = pos[s2] + jump
            re = pos[s2] + 2*jump
            #rs이상 re이하 pos 개수 -> cnt증가
            lower = BSLower(pos, s2+1, N-1, rs)
            if lower != -1 and pos[lower] <= re:
                upper = BSUpper(pos, lower, N-1, re)
                cnt += upper-lower+1
    return cnt

'''
def GetSolution():
    cnt = 0
    pos.sort()
    for s1 in range(N):
        for s2 in range(s1+1,N):
            jump = pos[s2] - pos[s1]
            rs = pos[s2] + jump
            re = pos[s2] + 2*jump
            for s3 in range(s2+1,N):
                if rs<=pos[s3]<=re:
                    cnt+=1
    return cnt
'''
sol = -1
# 입력받는 부분
N, pos = Input_Data()

# 여기서부터 작성
sol = GetSolution()
# 출력하는 부분
print(sol)