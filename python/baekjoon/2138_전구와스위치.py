'''
https://jshong1125.tistory.com/25
'''
import sys

readl = sys.stdin.readline
N = int(readl().strip())

currentLamp = list(map(int, readl().rstrip("\n")))
resultLamp = list(map(int, readl().rstrip("\n")))

def change(n):
    if n == 0:
        n = 1
    else:
        n = 0
    return n

def switch(n, cnt):
    count = cnt

    if count == 1:
        currentLamp[0] = change(currentLamp[0])
        currentLamp[1] = change(currentLamp[1])
    for i in range(1, N):
        if currentLamp[i-1] != resultLamp[i-1]:
            count += 1
            currentLamp[i-1] = change(currentLamp[i-1])
            currentLamp[i] = change(currentLamp[i])
            if i != N-1:
                currentLamp[i+1] = change(currentLamp[i+1])
    if currentLamp == resultLamp:
        return count
    else:
        return -1

res1 = switch(currentLamp[:], 0)
res2 = switch(currentLamp[:], 1)

if res1 >= 0 and res2 >= 0:
    print(min(res1,res2))
elif res1 >= 0 and res2 < 0:
    print(res1)
elif res1 < 0 and res2 >= 0:
    print(res2)
else:
    print(-1)