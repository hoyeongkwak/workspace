'''
입력
7
2 4 9 10 14 23 32
3
6 23 9

출력
0
6
3
'''
import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    data = [0] + list(map(int,readl().split()))
    T = int(readl())
    num = list(map(int,readl().split()))
    return N, data, T, num

def BS(list_data, s, e, d):
    while s <= e:
        m = (s+e) // 2
        if list_data[m] == d:
            return m
        elif list_data[m] > d:
            e = m - 1
        else:
            s = m + 1
    return -1

# 입력받는 부분
N, data, T, num = Input_Data()

# 여기서부터 작성
for n in num:
    ret = BS(data, 1, N, n)
    print(ret if ret != -1 else 0)
