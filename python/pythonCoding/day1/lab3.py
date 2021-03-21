import sys
def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    num = [float(readl()) for _ in range(N)]
    return N, num
sol = 0.0
# 입력받는 부분
N, num = input_data()
# 여기서부터 작성
nMax = 0

for i in range(N-1):
    n = num[i]
    for j in range(i+1,N):
        n = n * num[j]
        if n > nMax:
            nMax = n
sol = nMax

# 출력하는 부분

print(f"{sol:.3f}")