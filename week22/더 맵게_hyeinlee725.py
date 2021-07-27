import heapq
def solution(scoville, K):    
    answer = 0
    # 최소 heap
    heapq.heapify(scoville) # 기존의 배열을 heapify를 거쳐 heap으로 만듦

    # 가장 작은 scoville 지수가 K이상이 될 때까지
    while scoville[0] < K:
        try:
            min_scoville = heapq.heappop(scoville) # 가장 작은 scoville 지수
            second_scoville = heapq.heappop(scoville) # 두번째로 작은 scoville 지수
            mix_scoville = min_scoville + second_scoville *2
        except IndexError: # 예외 처리
            return -1 # len(scoville) <= 1인 경우
        heapq.heappush(scoville, mix_scoville)
        answer += 1
    return answer
