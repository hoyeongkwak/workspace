import sys
from bisect import bisect_left #이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려줌

readl = sys.stdin.readline

n = int(readl())
arr = list(map(int, readl().split()))
stack = [0]

for i in arr:
    if stack[-1] < i:
        stack.append(i)
    else:
        stack[bisect_left(stack, i)] = i
print(len(stack) - 1)