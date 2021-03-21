'''
입력 :
7
3 3 3 3 3 3 3 3 3 3

출력
3
2 1 0 0 0 0 0 0 0 0 
'''
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    cnt_box = list(map(int, readl().split()))
    return N, cnt_box

def Get_Solution():
    cnt_per_box = [1,  5,  10,  50,  100,  500,  1000,  3000,  6000,  12000]
    sol_box_cnt = [0] * len(cnt_per_box)
    total = sum([cnt_per_box[i] * cnt_box[i] for i in range(len(cnt_per_box))])
    p = total-N
    for i in range(len(cnt_per_box)-1, -1, -1):
        need = p // cnt_per_box[i]
        need = need if cnt_box[i] > need else cnt_box[i]
        sol_box_cnt[i] = cnt_box[i] - need
        p -= cnt_per_box[i]*need
    return sum(sol_box_cnt),  sol_box_cnt


sol = 0
sol_box_cnt = []

# 입력받는 부분
N,  cnt_box = input_data()

# 여기서부터 작성
sol,  sol_box_cnt = Get_Solution()

'''
Box 종류 : 1, 5, 10, 50, 100, 500, 1000, 3000, 6000, 12000
최대한 많은 Box
Box 개수

물품의 개수 N
박스의 개수 Ci 0<= ci <= 20

sum
1 * ci
5 * ci
...
sum > N end
'''
# 출력하는 부분
print(sol)
print(*sol_box_cnt)
