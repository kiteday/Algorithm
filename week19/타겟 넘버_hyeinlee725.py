from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((0, 0))
    while queue:
        sum_num, num_idx = queue.popleft()
        # pop한 index 값이 숫자가 담긴 배열 numbers의 len보다 작으면
        if(num_idx < len(numbers)):
            num = numbers[num_idx]
            # sum_num의 다음 idx에 위치한 numbers 원소를 + or - 한 위치 방문
            queue.append((sum_num + num, num_idx + 1))
            queue.append((sum_num - num, num_idx + 1))
        else: # pop한 sum_num이 마지막 원소이고, 값이 target과 같다면
            if(sum_num == target):
                answer += 1            

    return answer
