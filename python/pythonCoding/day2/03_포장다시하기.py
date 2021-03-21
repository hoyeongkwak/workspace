'''
입력
3
2 2 5

5
1 1 1 1 3

출력
13

15
'''

import sys
import heapq

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    candy = list(map(int,readl().split()))
    return N, candy

def Get_Solution():
    sol = 0
    for _ in range(N-1):
        candy.sort()
        c1 = candy.pop(0)
        c2 = candy.pop(0)
        sol += c1 + c2
        candy.append(c1+c2)
    return sol
#또 다른 솔루션
'''
def Get_Solution():
    sol = 0
    heapq.heapify(candy)
    for _ in range(N-1):
        candy.sort()
        c1 = heapq.heappop(candy)
        c2 = heapq.heappop(candy)
        sol += c1 + c2
        heapq.heappush(candy, c1+c2)
    return sol
'''


sol = -1
# 입력받는 부분
N, candy = Input_Data()

# 여기서부터 작성
sol = Get_Solution()

'''
sum = candy[0] + candy[1]
totalSum = sum
for i in range(2, N):
    candy.sort()
    sum = sum + candy[i]
    totalSum += sum
sol = totalSum
'''

# 출력하는 부분
print(sol)