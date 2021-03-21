import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_data = [list(map(int,readl().split()))for _ in range(N)]
    S = [list_data[n][0] for n in range(N)]
    A = [list_data[n][1] for n in range(N)]
    return N, S, A


sol = 0
# 입력받는 부분
N, S, A = Input_Data()

# 여기서부터 작성
for i in range(N):
    sol += (A[i] % S[i])

# 출력하는 부분
print(sol)