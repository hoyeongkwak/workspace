'''
입력
530

출력
4
'''
import sys

def Input_Data():
    readl = sys.stdin.readline
    change = int(readl())
    return change

def Get_Solution(change):
    cnt = 0
    coins = [500,100,50,10]
    for c in coins:
        cnt += change//c
        change%=c
    return cnt

sol = -1
# 입력받는 부분
change = Input_Data()

# 여기서부터 작성
sol = Get_Solution(change)

# 출력하는 부분
print(sol)

'''
거스름돈2

500 : 1
100 : 10
50 : 3
10 : 7
1460을 최대 동전갯수로 <-> (총금액-1460) 최소 동전갯수

'''