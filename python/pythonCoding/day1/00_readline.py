import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl().strip())
    list_s_a = []
    '''
    for n in range(N):
        list_s_a.append(list(map(int, readl().split())))
    '''
    #List Comprehensions
    list_s_a = [list(map(int, readl().split())) for n in range(N)]

    return N, list_s_a

N, list_s_a = Input_Data()
print(N)
print(list_s_a)