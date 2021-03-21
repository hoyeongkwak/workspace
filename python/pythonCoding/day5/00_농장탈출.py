'''
입력
5
522
6
84
7311
19

출력
3
'''
import sys


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    weight = [int(readl()) for _ in range(N)]
    return N, weight

def Check_Carry(A, B):
    while A and B:
        if A%10 + B%10 >= 10: return True
        A //= 10
        B //= 10
    return False

def DFS(s, sum_weight, cnt): #어떤소를 배에 태울것인가?
    global sol
    if cnt + (N-s) <= sol:
        return
    if sol < cnt:
        sol = cnt

    for n in range(s, N):
        #n번 소를 태우는 시도!
        if not Check_Carry(sum_weight, weight[n]):
            DFS(n+1, sum_weight + weight[n], cnt+1)

'''
def DFS(n, sum_weight, cnt): #각각의 소 -> 태울것?(자리올림이 발생하지 않을때!) 말것?(언제든지!)
    global sol
    #가지치기 조건
    if cnt + (N-n) <= sol:
        return

    if n>=N:
        if sol < cnt:
            sol = cnt
        return

    #태우기!
    if not Check_Carry(sum_weight, weight[n]):
        DFS(n+1, sum_weight + weight[n], cnt + 1)

    #안태우기!
    DFS(n+1, sum_weight, cnt)
'''

sol = -1
# 입력받는 부분
N, weight = input_data()

# 여기서부터 작성
#DFS(n, sum_weight, cnt)
DFS(0,0,0)


# 출력하는 부분
print(sol)