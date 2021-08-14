def change(music): # '#'이 붙은 음을 소문자로 변경하는 함수
    if ('A#' in music):
        music = music.replace('A#', 'a')
    if ('F#' in music):
        music = music.replace('F#', 'f')
    if ('C#' in music):
        music = music.replace('C#', 'c')
    if ('G#' in music):
        music = music.replace('G#', 'g')
    if ('D#' in music):
        music = music.replace('D#', 'd')
    return music

# m : 네오가 기억한 멜로디를 담은 문자열
# musicinfos : 방송된 곡의 정보를 담고 있는 배열
def solution(m, musicinfos):
    answer = []
    m = change(m)
    for info in musicinfos:
        # 시작한 시각, 끝난 시각, 음악 제목, 악보 정보 문자열 input(,로 구분)
        start, end, music_title, melody = info.split(',')
        # 음악 시작 시각, 끝난 시각(24시간 'HH:MM')을 시간과 분으로 받음
        start_hour, start_min = start.split(':')
        end_hour, end_min = end.split(':')
        # 재생 시간 계산
        time = (int(end_hour) - int(start_hour)) * 60 + (int(end_min) - int(start_min))
        melody = change(melody) # 악보에 붙은 #을 소문자로 변경
        # 악보 재생정보
        if (len(melody) >= time):
            melody_played = melody[:time]
        else:
            melody_played = (melody * time)[:time]
        # 기억한 멜로디가 재생된 악보에 있다면
        if (m in melody_played):
            # answer 배열에 재생 시간과 음악 제목 추가
            answer.append([time, music_title])
    # 조건에 일치하는 음악이 여러 개일 때
    if (len(answer) >= 1):
        # 재생된 시간이 제일 긴 음악 제목을 기준으로 정렬
        answer = sorted(answer, key = lambda x: (-x[0]))
        # 음악 제목 반환
        return answer[0][1]
    # 조건이 일치하는 음악이 없을 때
    else:
        # "(None)" 반환
        return "(None)"
