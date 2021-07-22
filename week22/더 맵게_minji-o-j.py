'''
힙
- 최댓값과 최솟값을 빠르게 찾을 수 있음
- 완전 이진 트리 형태, 부모간의 대소관계 성립(루트는 가장 큰 노드이거나 가장 작은 노드)
- 새로운 데이터를 추가할 때 사용하기 좋음
- 완전 이진 형태라서 연결리스트보다는 배열로 구현
- 파이썬에선 heapq 사용
https://www.daleseo.com/python-heapq/
'''
import heapq
def solution(scoville, K):
    heapq.heapify(scoville) #list를 heap 모양으로 변경, 시간복잡도 O(N)
    count=0 #몇번 섞을지 count

    # 가장 작은 원소가 K보다 클 때까지
    while scoville[0]<K:
        # 원소가 1개인데 K보다 작을 경우 -1 반환
        if len(scoville)<=1:
            return -1
        min1=heapq.heappop(scoville)
        min2=heapq.heappop(scoville)
        new_s=min1+min2*2
        heapq.heappush(scoville,new_s)
        count+=1

    return count
