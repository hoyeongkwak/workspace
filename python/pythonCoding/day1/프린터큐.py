import sys

def input_data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    job = list(map(int, readl().split()))
    return N, M, job


T = int(sys.stdin.readline())
sol = []
for _ in range(T):
    #입력받는 부분
    N, M, job = input_data()
    # 여기서부터 작성
    cnt = 0
    while job:
        top = max(job)
        M -= 1
        pop = job.pop(0)
        if top != pop:
            job.append(pop)
            if M < 0:
                M = len(job) -1
        else:
            cnt+=1
            if M == -1:
                print(cnt)
                break

