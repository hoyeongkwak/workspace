'''
반례
https://bingorithm.tistory.com/3
'''
import sys

readl = sys.stdin.readline
n = int(readl().strip())

plst = []
nlst = []
onelst = []

for i in range(n):
    num = int(readl().strip())
    if num > 1:
        plst.append(num)
    elif num <= 0:
        nlst.append(num)
    else:
        onelst.append(num)

plst.sort(key=lambda x:-x)
nlst.sort()

total = 0

if len(plst) % 2 == 0:
    for i in range(0, len(plst), 2):
        total += (plst[i] * plst[i+1])
else:
    for i in range(0, len(plst)-1, 2):
        total += (plst[i] * plst[i+1])
    total += plst[len(plst)-1]

if len(nlst) % 2 == 0:
    for i in range(0, len(nlst), 2):
        total += (nlst[i] * nlst[i+1])
else:
    for i in range(0, len(nlst)-1, 2):
        total += (nlst[i] * nlst[i+1])
    total += nlst[len(nlst)-1]

total += sum(onelst)

print(total)
