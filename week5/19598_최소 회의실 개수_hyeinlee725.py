import sys

# 첫째 줄에 배열의 크기 N(1 ≤ N ≤ 100,000)
N = int(sys.stdin.readline()) # N개의 회의

time = [] # 회의시간 저장 배열

# 둘째 줄부터 N+1 줄까지 공백을 사이에 두고 회의의 시작시간과 끝나는 시간
for _ in range(N):
    start, finish = map(int, input().split())
    time.append((start, 1)) # 회의 시작(+1)
    time.append((finish, -1)) # 회의 종료(-1)
time.sort() # 오름차순으로 정렬

count = 0 # 회의실 개수 count 
room = 0 # 최소 회의실 개수

for i, j in time: # time 내에 있는 변수 내에서
    # count에 j를 더해줌(회의실 개수)
    count += j
    room = max(room, count) # 최종으로 max값을 출력

print(room) # 최소 회의실 개수를 출력
