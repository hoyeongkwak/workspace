'''
입력
4
-15 5
-10 36
10 73
27 44

53
1 6
1 31
-54 47
60 134
174 352
207 645
3135 3942
5397 7618
141 8080
0 0
0 8
5 48
88 93
198 396
25

출력
2

13


4
10 73
-10 36
-15 5
27 44
'''

import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    chems = [list(map(int,readl().split())) for _ in range(N)]
    return N, chems
def GetSolution():
    chems.sort()
    min, max = chems[0][0], chems[0][1]
    cnt = 1
    for i in range(1,N):
        smin, smax = chems[i][0], chems[i][1]
        if min < smin:
            min = smin
        if max > smax:
            max = smax
        if smin > max:
            cnt += 1
            min, max = smin, smax
    return cnt
'''
def GetSolution():
    chems.sort()
    ref_e = chems[0][1]
    cnt_ref = 1
    for s,e in chems[1:]:
        if ref_e >= s:
            if ref_e > e:
                ref_e = e
        else:
            cnt_ref += 1
            ref_e = e
    return cnt_ref
'''


sol = 0

# 입력받는 부분
N, chems = input_data()

# 여기서부터 작성
sol = GetSolution()
'''
N : 화학 물질의 수
chems : 보관 최저, 최고온도
!!최소수를 구함!!

정렬이 필요
최저온도로 정렬

A[0] = -15   A[1] = 5
A[0] < B[0]  A[1] < B[1] O
A[0] < C[0]  A[1] < C[1]

 
A[0] < C[0]  B[1] < C[1] 

A : -15        5
B : -10        36
c : 10         73
d : 27         44

최소 냉장고의 수
'''

# 출력하는 부분

print(sol)