# 이분 탐색
def solution(stones, k):
    answer = -1
    left = 1
    right = max(stones)
    while (left <= right): # left가 right이하일 때 반복
        # 징검다리를 건널 수 있는 수(mid)
        mid = (left + right) // 2
        cnt = 0
        for s in stones:
            # 0 이하이면 cnt + 1
            if (s - mid <= 0):
                cnt += 1
            else: # 0보다 큰 원소가 있다면
                cnt = 0 # 0으로 초기화
            if (cnt >= k):
                break
        # cnt가 k와 같거나 크다면 right를 mid - 1로 내림
        if (cnt >= k):
            right = mid - 1
        # 그렇지 않으면 left를 mid + 1로 올림
        else: 
            left = mid + 1
            # 최대 몇 명 까지 징검다리를 건널 수 있는지 return
            answer = max(answer, mid + 1)
    return answer
