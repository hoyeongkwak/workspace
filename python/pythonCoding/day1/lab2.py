import sys

def Input_Data():
    readl = sys.stdin.readline
    s = input().strip()
    return s


sol = 5

# 입력받는 부분
s = Input_Data()

# 여기서부터 작성
bBottom = False
bTop = False
for i in s:
    n = 5
    if i == '(':
        bBottom = True
        if bTop == True:
            n += 5
        bTop = False
    elif i == ')':
        bTop = True
        if bBottom == True:
            n += 5
        bBottom = False
    sol += n
# 출력하는 부분
print(sol)