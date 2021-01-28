'''
python으로는 계속 시간초과 나서 pypy3로만 성공했어 ㅜㅜ
'''

import sys
import heapq

N = int(sys.stdin.readline())
meeting = [] #heapq 형태로 사용할 것
room = [] #end(회의 끝나는 시간)만 들어가있음

for _ in range(N):
    heapq.heappush(meeting, list(map(int, sys.stdin.readline().split())))

while len(meeting)!=0:
    flag = True #회의실의 점유 유무 판단용 (False면 기존회의실 사용가능, True면 회의실 추가)
    st, end = heapq.heappop(meeting)
    
    #맨 처음에 회의실 하나 추가
    if not room:
        room.append(end)
        
    else:    
        for i in range(len(room)):
            if room[i] <= st: #이미 회의가 끝나있는 회의실이 있으면
                room[i] = end #거기 사용하고 끝나는시간 update
                flag = False
                break
            
        if flag == True: #사용가능한 회의실이 없으면
            room.append(end) #회의실 추가(끝나는시간 기록)
            
print(len(room))