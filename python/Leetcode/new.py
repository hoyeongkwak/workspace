'''
https://gglifer-cs.tistory.com/41
https://hibee.tistory.com/205
'''
matrix = [['x','x','.','x'],['.','x','.','x'],['x','x','.','x'],['x','x','.','x']]
row = len(matrix)
col = len(matrix[0])
def checkClear():
    newList = ['.','.','.','.']
    for n in matrix[:]:
        if n.count('x') == 4:
            matrix.remove(n)
            matrix.insert(0,newList)
def is_ok(x, y):
    for i in range(x, row):
        if matrix[i][y] == 'x' or x == row - 1:
            return False
    return True
'''
    if x == row - 1 and y == col - 1:
        return False
    if matrix[x][y-1] == 'x' or matrix[x+1][y] == 'x':
        return False
'''



def shape2():
    for c in range(col):
        for r in range(row):
            if matrix[r][c] == '.' and r < row -1 and 0 < c < col:
                if matrix[r+1][c] == '.' and matrix[r][c-1] == '.' and is_ok(r,c) == True:
                    matrix[r][c] = 'x'
                    matrix[r+1][c] = 'x'
                    matrix[r][c-1] = 'x'

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
shape2()
#checkClear()
print(matrix)



