'''
입력
0 32
3 13
28 25
39 0

출력
42
'''
import sys

def Input_Data():
    readl = sys.stdin.readline
    list_inout = [list(map(int,readl().split())) for _ in range(4)]
    return list_inout
'''

def Get_Solution():
    max_passenger = 0
    passenger = 0
    for n in range(4):
        passenger = passenger - list_inout[n][0] + list_inout[n][1]
        if max_passenger < passenger:
            max_passenger = passenger
    return max_passenger
 
'''


def GetSolution():
    cnt = 0
    maxCnt = 0
    for oCnt, iCnt in list_inout:
        cnt += (iCnt - oCnt)
        if maxCnt < cnt:
            maxCnt = cnt
    return maxCnt
'''
def GetSolution():
    max_passenger = 0
    passenger =0
    for n in range(4):
'''



sol = -1
#입력받는 부분
list_inout = Input_Data()

#여기서 부터 작성
'''
4개의 역
list_inout = (내린사람의 수, 탄 사람의수)
기차 안에 가장 많은 사람의 수
'''

sol = GetSolution()


#출력 하는 부분
print(sol)