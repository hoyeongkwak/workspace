'''
https://jshong1125.tistory.com/25
'''
import sys
readl = sys.stdin.readline
n = int(readl().strip())

curLamp = list(map(int,readl().strip()))
reLamp = list(map(int, readl().strip()))

def change(n):
    if n == 1:
        n = 0
    else:
        n = 1
    return n

def switch(lst, cnt):
    count = cnt
    if count == 1:
        lst[0] = change(lst[0])
        lst[1] = change(lst[1])

    for i in range(1, n):
        if lst[i-1] != reLamp[i-1]:
            lst[i-1] = change(lst[i-1])
            count += 1
            lst[i] = change(lst[i])
            if i != n-1:
                lst[i+1] = change([i+1])
    if lst == reLamp:
        return count
    else:
        return -1

res1 = switch(curLamp[:], 0)
res2 = switch(curLamp[:], 1)

if res1 >= 0 and res2 >=0:
    print(min(res1, res2))
elif res1 >= 0 and res2 < 0:
    print(res1)
elif res1 < 0 and res2 >= 0:
    print(res2)
else:
    print(-1)



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

def switch(c, cnt):
    count = cnt
    if count == 1:
        c[0] = change(c[0])
        c[1] = change(c[1])
    for i in range(1, N):
        if c[i-1] != resultLamp[i-1]:
            count += 1
            c[i-1] = change(c[i-1])
            c[i] = change(c[i])
            if i != N-1:
                c[i+1] = change(c[i+1])
    if c == resultLamp:
        return count
    else:
        return -1

res1 = switch(currentLamp[:], 0)
res2 = switch(currentLamp[:], 1)

if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))
elif res1 >= 0 and res2 < 0:
    print(res1)
elif res1 < 0 and res2 >= 0:
    print(res2)
else:
    print(-1)
'''