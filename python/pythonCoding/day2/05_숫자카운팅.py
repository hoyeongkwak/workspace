'''
입력
10
1 1 1 6 9 11 13 17 19 20
2
1 9

출력
3 1
'''
import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    data = [0] + list(map(int,readl().split()))
    T = int(readl())
    num = list(map(int,readl().split()))
    return N, data, T, num

def BS_lower(list_data, s, e, d):
    sol = -1
    while s <= e:
        m = (s+e)//2
        if list_data[m] == d:
            sol = m
            e = m-1
        elif list_data[m] > d:
            e = m-1
        else:
            s = m+1
    return sol


def BS_upper(list_data, s, e, d):
    sol = -1
    while s <= e:
        m = (s+e)//2
        if list_data[m] == d:
            sol = m
            s = m+1
        elif list_data[m] > d:
            e = m-1
        else:
            s = m+1
    return sol


# 입력받는 부분
N, data, T, num = Input_Data()

# 여기서부터 작성
for n in num:
    lower = BS_lower(data, 1, N, n)
    if lower != -1:
        upper = BS_upper(data, 1, N, n)
        print(upper-lower+1, end = " ")
    else: print(0,end = " ")

