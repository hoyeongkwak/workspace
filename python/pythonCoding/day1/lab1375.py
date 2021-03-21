import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    str_exp = readl().split()
    nums = list(map(int,str_exp[0::2]))
    op = str_exp[1::2]
    return N, nums, op

def Cal_Expression(nums, op):
    result = 0
    stack = []
    stack.append(nums[0])
    for o,n in zip(op, nums[1:]):
        if o == '+':
            stack.append(n)
        elif o == '-':
            stack.append(-n)
        elif o == '*':
            stack.append(stack.pop() * n)
        elif o == '/':
            stack.append(int(stack.pop() / n))

    for n in stack:
        result += n
    return result

sol = -1
# 입력받는 부분
N, nums, op = Input_Data()

# 여기서부터 작성
sol = Cal_Expression(nums, op)
'''
tmpStack = []
tmpStack.append(nums[0])

for i in range(1, N):
    if op[i-1] == '+':
        tmpStack.append(nums[i])
    elif op[i-1] == '-':
        tmpStack.append(-nums[i])
    elif op[i-1] == '*':
        tmpStack[i-1] = (tmpStack[i-1] * nums[i])
    elif op[i-1] == '/':
            if tmpStack[i-1] // i < 0:
                tmpStack[i-1] = ((tmpStack[i-1] // nums[i]) + 1)
            else:
                tmpStack[i-1] =(tmpStack[i-1] // nums[i])
for i in tmpStack:
    sol += i
'''
# 출력하는 부분
print(sol)