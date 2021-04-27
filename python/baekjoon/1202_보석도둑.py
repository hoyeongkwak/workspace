import sys
import heapq
readl = sys.stdin.readline

n, k = map(int, readl().split())
gem = []
bag = []

for _ in range(n):
    w, v = map(int, readl().split())
    heapq.heappush(gem, [w,v])

for _ in range(k):
    c = int(readl())
    heapq.heappush(bag, c)

total = 0
c_gem = []

for _ in range(k):
    c = heapq.heappop(bag)

    while gem and c_gem >= gem[0][0]:
        [w,v] = heapq.heappop(gem)
        heapq.heappush(c_gem, -v)
    if c_gem:
        total -= heapq.heappop(c_gem)
    elif not gem:
        break
print(total)
'''
readl = sys.stdin.readline
n, k = map(int, readl().split())
gem = []
bag = []
for _ in range(n):
    weight, value = map(int, readl().split())
    heapq.heappush(gem, [weight,value])
for _ in range(k):
    capacity = int(readl())
    heapq.heappush(bag, capacity)

total = 00
capable_gem = []

for _ in range(k):
    capacity = heapq.heappop(bag)

    while gem and capacity >= gem[0][0]:
        [weight, value] = heapq.heappop(gem)
        heapq.heappush(capable_gem, -value)
    if capable_gem:
        total -= heapq.heappop(capable_gem)
    elif not gem:
        break
print(total)
'''
