# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque


def input_data():
    readl = sys.stdin.readline
    N,  S,  M = map(int,  readl().split())
    return N,  S,  M

def solve():
    sol_list = []
    q = deque(list(range(S,  N+1))+list(range(1, S)))

    for _ in range(N):
        for _ in range(M-1):
            q.append(q.popleft())
        sol_list.append(q.popleft())
    return sol_list


sol_list = []

# 입력받는 부분
N,  S,  M = input_data()

# 여기서부터 작성
sol_list = solve()

# 출력하는 부분
print(*sol_list)
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque


def input_data():
    readl = sys.stdin.readline
    N,  S,  M = map(int,  readl().split())
    return N,  S,  M

def solve():
    sol_list = []
    q = deque(list(range(S,  N+1))+list(range(1, S)))

    for _ in range(N):
        q.rotate(-M+1)
        sol_list.append(q.popleft())
    return sol_list


sol_list = []

# 입력받는 부분
N,  S,  M = input_data()

# 여기서부터 작성
sol_list = solve()

# 출력하는 부분
print(*sol_list)
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque


def input_data():
    readl = sys.stdin.readline
    N,  S,  M = map(int,  readl().split())
    return N,  S,  M

def solve():
    sol_list = []
    list_man = list(range(1, N+1))
    idx = S-1
    for _ in range(N):
        idx = (idx+(M-1)) % len(list_man)
        sol_list.append(list_man.pop(idx))
    return sol_list

sol_list = []

# 입력받는 부분
N,  S,  M = input_data()

# 여기서부터 작성
sol_list = solve()

# 출력하는 부분
print(*sol_list)