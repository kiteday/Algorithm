''' 
[프로그래머스] 더 맵게
정확성: 76.2
효율성: 23.8
재귀함수는 효율성 0, 정확성은 부분 틀렸다고 뜸 
'''
import heapq

def solution(scoville, K):
    heapq.heapify(scoville) # 배열을 힙 자료형으로 바꾸기
    answer = 0
    
    while(len(scoville) >= 2): # 모든 음식을 섞었다면 탈출
        a = heapq.heappop(scoville) # 가장 안매운 음식
        b = heapq.heappop(scoville) # 두번째로 안매운 음식
        heapq.heappush(scoville, a + (b * 2)) # 음식 섞기
        answer += 1  

        if scoville[0] >= K :
            break;

    # 모든 음식을 합쳐도 원하는 스코빌 지수로 만들 수 없다면
    if scoville[0] < K:
        return -1
    # 모든 음식이 원하는 스코빌 지수라면
    else:
        return answer