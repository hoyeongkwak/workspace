import sys

readl = sys.stdin.readline

N = int(readl().strip())

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

s = factorial(N)
print(s)



