from collections import deque
def solution(progresses, speeds):
    answer = []
    p = deque(progresses)
    s = deque(speeds)
    while p:
        for i in range(len(p)):
            p[i] += s[i]
        tmp = 0

        while p and p[0] >= 100:
            p.popleft()
            s.popleft()
            tmp += 1

        if tmp != 0:
            answer.append(tmp)
    return answer




print(solution([93,30,55],[1,30,5])) #[2,1]
#print(solution([95,90,99,99,80,99],[1,1,1,1,1,1])) #[1,3,2]
