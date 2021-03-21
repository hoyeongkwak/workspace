'''
입력
10
8 24 27 18 20 6 17 19 30 11

출력
6 8 11 17 18 19 20 24 27 30
'''
import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    A = list(map(int,readl().split()))
    return N, A

# 입력받는 부분
N, A = Input_Data()

# 여기서부터 작성
#오름차순
#A.sort()
#B = sorted(A)

#내림차순
A.sort(key=lambda x:-x)
#B = sorted(A, key=lambda x:-x)



# 출력하는 부분
print(*A)
#print(*B)