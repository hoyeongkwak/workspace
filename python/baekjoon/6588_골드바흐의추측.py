import sys

readl = sys.stdin.readline
N = -1

def isPrime(a):
    if a < 2:
        return False
    for i in range(2,a):
        if a%i == 0:
            return False
    return True

while N != 0:
    N = int(readl())

    if N == 0:
        break
    nList = []
    max = [0,0,0]
    for i in range(N+1):
        if isPrime(i):
            nList.append(i)

    for j in range(len(nList)):
        for k in range(j, len(nList)):
            if (nList[j] + nList[k]) == N:
                if (max[1]-max[0]) < (nList[k] - nList[j]):
                    max[0], max[1] = nList[j], nList[k]
    if max[0] == 0 and max[1] == 0:
        print("Goldbach's conjecture is wrong.")
    else:
        print(N, " = ", max[0], "+", max[1])
