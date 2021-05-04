import sys

#readl = sys.stdin.readline

def solution(numbers, target):
    answer = 0
    templst = numbers.copy()
    for i in range(len(numbers)):
        templst[i] = -templst[i]
        if sum(templst) == target:
            answer += 1
        for j in range(i+1, len(numbers)):
            templst[j] = -templst[j]
            if sum(templst) == target:
                answer += 1
        templst = numbers.copy()
    return answer

#sol = solution([1,1,1,1,1], 3)
print(solution([1, 1, 1, 1, 1], 3), 5)
print(solution([1, 2, 1, 2], 2), 3)
print(solution([1, 2, 1, 2], 6), 1)
#print(sol)
