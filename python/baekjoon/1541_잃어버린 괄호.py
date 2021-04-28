import sys

readl = sys.stdin.readline
n = readl().split("-")
num = []

for i in n:
    cnt = 0
    s = i.split("+")
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)

