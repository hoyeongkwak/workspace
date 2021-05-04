from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    q = deque()
    for _ in range(bridge_length):
        q.append(0)
    while q:
        answer += 1
        q.popleft()

        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return answer

'''
    q = [0] * bridge_length
    time = 0

    while q:
        time += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return time
'''


print(solution(2, 10, [7,4,5,6])) # return 8
#print(solution(100, 100, [10])) # return 101
#print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10])) # return 110
