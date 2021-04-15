import sys

readl = sys.stdin.readline
N = int(readl().strip())
list = []
cnt = 0
for _ in range(N):
    s, e = readl().split()
    list.append([int(s), int(e)])
list.sort(key = lambda x:(x[1], x[0]))
st, et = 0, 0
for i in list:
    if i[0] >= et:
        st, et = i[0], i[1]
        cnt += 1

print(cnt)