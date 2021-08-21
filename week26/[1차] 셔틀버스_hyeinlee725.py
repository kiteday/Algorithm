def solution(n, t, m, timetable):
    answer = ''
    # 크루 대기열 도착시간 - 분 단위로 계산, 정렬
    crew_time = [int(time.split(":")[0]) * 60 + int(time.split(":")[1]) for time in timetable]
    crew_time.sort()
    # 버스 탑승 시간, 탑승자, 마지막 탑승 시간
    bus = [[9 * 60 + i * t, int(m), 0] for i in range(n)]
    crew_idx, bus_idx = 0, 0 # 각각 crew_time, bus index
    # 운행 횟수가 남아있거나 시간이 있으면
    while n > 0 and crew_time:
        # crew_idx가 도착 시간과 같거나 bus_idx가 운행 횟수와 같으면 종료
        if (crew_idx == len(crew_time) or bus_idx == n):
            break
        # 시간이 맞고, 탑승할 수 있는 자리가 남아있을 때
        if (crew_time[crew_idx] <= bus[bus_idx][0] and bus[bus_idx][1] > 0):
            # 마지막 탑승 시간 변경
            bus[bus_idx][2] = crew_time[crew_idx]
            bus[bus_idx][1] -= 1 # 탑승 가능 인원 줄이기
            crew_idx += 1 # 도착시간 +
        else:
            bus_idx += 1
    res = bus[-1][0]
    # 버스에 자리가 없을 때
    if(bus[-1][1] == 0):
        # 마지막 승객보다 1분 빠른 시간
        res = bus[-1][2] -1
    else: # 자리가 있다면 마지막 시간
        res = bus[-1][0]
    answer = "%02d:%02d" % (res // 60, res % 60)
    return answer
