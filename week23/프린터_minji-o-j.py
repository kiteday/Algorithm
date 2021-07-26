from collections import deque #deque 사용 위함
def solution(priorities, location):
    p_index=0 #정렬한 배열에서 현재 위치 index
    track_location=location #location 위치 따라다님
    answer = 1 #count
    
    sort_p=sorted(priorities,reverse=True) #큰 순 정렬한 배열
    p_queue=deque(priorities) #deque 형태로 바꿈
    
    while True:
        if sort_p[p_index]==p_queue[0]: #현재 맨 앞에 있는 것이 최대 우선 순위 만족함
            p_index+=1
            p_queue.popleft() #원소 제거
            
            
            if track_location==0: #제거해야 할 것이 맨 앞에 있었으면
                break
            else: #맨 앞에 있지 않았음
                track_location-=1
                answer+=1 #1회 시행
                
        else: #현재 맨 앞에 있는 것이 최대 우선 순위 만족하지 못함
            p_queue.append(p_queue.popleft()) #빼서 다시 넣음
            if track_location==0: #맨 앞에 있던것이 빠졌었을 경우
                track_location=len(p_queue)-1 #index 맨 뒤로 이동
            else:
                track_location-=1
    return answer
