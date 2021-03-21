import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    job = map(int, readl().split())
    return N, M, job

def solve(N, M, job):
    q = deque()
    cnt_prio = [0] * 10

    for idx, prio in enumerate(job):
        q.append((idx, prio))
        cnt_prio[prio]+=1

    cnt = 0
    for loop_prio in range(9,0,-1):
        for _ in range(cnt_prio[loop_prio]):
            while 1:
                idx , prio = q.popleft()
                if prio == loop_prio: break
                q.append((idx, prio))
            cnt+=1
            if idx == M: return cnt

    return -1


T = int(sys.stdin.readline())
sol = []
for _ in range(T):
    #입력받는 부분
    N, M, job = input_data()

    # 여기서부터 작성
    ret = solve(N, M, job)
    sol.append(str(ret))

print("\n".join(sol))