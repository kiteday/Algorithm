'''
[프로그래머스] [1차] 셔틀버스
정확성 : 100.0
'''
import heapq
# 탑승
def bording(crew, cur_time, m):
    occupant = -1 
    
    while m > 0:
        occupant = heapq.heappop(crew)
        
        if occupant <= cur_time: # 도착시간 보다 빨리 도착한 크루들 탑승
            m -= 1
        else:
            heapq.heappush(crew, occupant)
            return -1
        
        if not crew and m > 0: # 모든 버스가 오기전에 전부 탑승했다면
            return -1 

    return occupant

def solution(n, t, m, timetable):
    crew = []
    cur_time = 9 * 60 # 09:00
    
    # 우선 정렬 큐
    for i in timetable: 
        time = int(i[0]) * 10 * 60 + int(i[1]) * 60 + int(i[3]) * 10 + int(i[4])
        heapq.heappush(crew, time);    
    
    # 버스에 탑승 시키기 시작
    while n > 0 and crew:
        last = bording(crew, cur_time, m)
        n -= 1
        cur_time += t
    
    # 막차까지 버스가 가득차있지 않다면
    if last == -1:
        last = cur_time - t
    # 만석이었다면 마지막 승객보다 1분 빨리오기 
    else :
        last -= 1
    
    # 콘이 도착해야할 시간 int to str
    hour = last // 60
    minute = last % 60
    if hour < 10 :
        hour = '0' + str(hour)
    if minute < 10 :
        minute = '0' + str(minute)
    
    answer = str(hour) + ':' + str(minute)
        
    return answer
