'''
https://gglifer-cs.tistory.com/41
https://hibee.tistory.com/205

l     ll       ll         l             l
l      l       l         ll             ll
l
'''
#matrix = [['x','x','.','x'],['.','x','.','x'],['x','x','.','x'],['x','x','.','x']]
import collections
matrix = [['.', '.', '.', '.'],['x','x','.','x'],['x','.','.','x'],['x','x','.','.'],['x','x','.','.']]
row = len(matrix)
col = len(matrix[0])
v = collections.deque()
ans = 0
shape = [[0,0],[0,1],[1,1]]

def dfs(r, c, cnt):
    global ans
    global v
    if cnt == 3:
        flag = True
        for i in range(len(v)):
            x = v[i][0]
            y = v[i][1]
            if is_ok(x,y):
                flag = False
                break
        if flag == False:
            for i in range(len(v)):
                x = v[i][0]
                y = v[i][1]
                matrix[x][y] = 'x'

        #if flag == True:
        #    ans+= 1

        return
    nx = r + shape[cnt][0]
    ny = c + shape[cnt][1]

    if nx < 0 or ny < 0 or nx >= row or ny >= col:
        return
    if matrix[nx][ny] == 'x':
        return
    v.appendleft(([nx,ny]))
    #matrix[nx][ny] = '-'
    dfs(r,c, cnt+1)
    #matrix[nx][ny] = '.'
    v.pop()
    return

def is_ok(x, y):
    for i in range(0, x):
        if matrix[i][y] == 'x':
            return False
    if matrix[x][y] == 'x' or x == row - 1:
        return False
    return True

def checkClear():
    newList = ['.','.','.','.']
    for n in matrix[:]:
        if n.count('x') == 4:
            matrix.remove(n)
            matrix.insert(0,newList)

    for n in range(row):
        for m in range(col):
            print(n,m)

for i in range(row):
    for j in range(col):
        dfs(i, j, 0)
'''
    if x == row - 1 and y == col - 1:
        return False
    if matrix[x][y-1] == 'x' or matrix[x+1][y] == 'x':
        return False
'''

'''
    for c in range(col):
        for r in range(row):
            if matrix[r][c] == '.' and r < row -1 and 0 < c < col:
                if matrix[r+1][c] == '.' and matrix[r][c-1] == '.' and is_ok(r,c) == True:
                    matrix[r][c] = 'x'
                    matrix[r+1][c] = 'x'
                    matrix[r][c-1] = 'x'
'''
def shape1():
    for c in range(col):
        ret = 0
        for r in range(row):
            if matrix[r][c] == '.':
                ret+= 1
                if r < row and ret > 2:
                    if is_ok(r,c) == False:
                        matrix[r][c] = 'x'
                        matrix[r-1][c] = 'x'
                        matrix[r-2][c] = 'x'
                        ret = 0
#shape1()
#shape2()
#checkClear()
#for i in range(len(matrix)):
#    print(matrix[i])
checkClear()
#print("========================")
#for i in range(len(matrix)):
#    print(matrix[i])