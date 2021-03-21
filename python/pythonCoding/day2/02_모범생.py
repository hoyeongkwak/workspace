'''
입력
8
70 30 70 40 60 50 90 80
출력
7 8 1
'''
import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    score = map(int,readl().split())
    info = list(enumerate(score, 1))
    return N, info

# 입력받는 부분
N, info = Input_Data()

# 여기서부터 작성
info.sort(key=lambda x:(-x[1], x[0]))

# 출력하는 부분
for n in range(3):
    print(info[n][0], end = ' ')