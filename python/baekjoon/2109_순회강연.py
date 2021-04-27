import sys
import heapq

readl = sys.stdin.readline
n = int(readl())
lecList = []
day = 0
total = 0
for i in range(n):
    lecList.append(list(map(int, readl().split())))
lecList.sort(key=lambda x:x[1])
p_list = []

for i in lecList:
    heapq.heappush(p_list, i[0])
    if len(p_list) > i[1]:
        heapq.heappop(p_list)
print(sum(p_list))
