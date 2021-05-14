# [1034] 램프
import sys
N, M = map(int, input().split()) # 행, 열
lamp = [input() for _ in range(N)]
K = int(input()) # 스위치를 누르는 횟수
result = 0 # 결과

for i in range(N):
    lamp_out, ramp_raw_on = 0, 0 # 꺼져있는 램프 개수, 켜져있는 램프의 열 개수

    lamp_out = lamp[i].count('0') # 꺼져있는 램프 개수 세기

    '''
    lamp_out <= k :램프가 꺼져있는 개수가 더 많으면 행의 램프를 다 킬 수 없음
    lamp_out % 2 == k % 2 : 스위치를 짝수번 눌렀을 때 처음이와 같은 결과가 나오므로 나머지 값이 같아야한다.
    '''
    if lamp_out <= K and lamp_out % 2 == K % 2:
        for j in range(N):
            if(lamp[i] == lamp[j]): # 다른 행의 모양이 같으면 똑같이 켜지니 count한다
                ramp_raw_on += 1
    result = max(ramp_raw_on, result)

print(result)
