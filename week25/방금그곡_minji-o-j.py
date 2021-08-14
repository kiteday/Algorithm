import re

def solution(m, musicinfos): #m: 네오가 기억한 멜로디, musicinfos: 방송된 곡의 정보를 담은 배열
    answer=[]
    for music in musicinfos:
        ## 배열로 변환
        music=music.split(',')
        
        ## 배열 가져오기
        music_start=re.sub(':','',music[0]) #: 제거, 재생 시작시간
        music_finish=re.sub(':','',music[1]) #: 제거, 재생 끝나는 시간
        music_name=music[2] # 음악 제목
        music_score=music[3] # 악보 정보(멜로디 정보)
        score_len=len(re.sub('#','',music[3])) # 악보 길이
        
        ## 재생 시간 계산
        music_time=(int(music_finish[:2])-int(music_start[:2]))*60\
                    +int(music_finish[2:])-int(music_start[2:])

        ## 재생 시간에 맞춘 악보
        if music_time>=score_len:
            if music_time%score_len==0: #나눠 떨어지면
                 score_repeat=music_time//score_len
            else: # 안나눠떨어짐
                score_repeat=music_time//score_len+1
                
            score_play='' # 재생될 것으로 예상되는 악보(반복 포함)
            for _ in range(score_repeat):
                score_play+=music_score
                
        else: # 재생 시간보다 악보 길이가 짧으면
            score_play=''
            index=0
            count=0
            while count<music_time: #문자열 cut용
                if music_score[index]!='#':
                    score_play+=music_score[index]
                    index+=1
                    count+=1
                    if (count)==music_time: # 마지막글자 # 까지 자르기 위한 조건
                        if music_score[index]=='#':
                            score_play+='#'
                        
                else:
                    score_play+=music_score[index]
                    index+=1

        ## 문자열 안에 있나 검사
        find_index=0 #find 시작 index
        m_len=len(m)
        
        while True:
            in_score=score_play[find_index:].find(m) # score_play 안에 m이 있나?
            
            if in_score==-1: #없으면
                break
                
            else: #있음
                # print(score_play[find_index+in_score:find_index+in_score+m_len]) #찾은 위치
                if find_index+in_score+m_len<len(score_play): # 추가 문자열 검사가 가능함
                    if score_play[find_index+in_score+m_len]=='#': # 추가로 '#'이 붙어 있는 경우
                        find_index+=m_len
                        continue #안담음
                    else: # '#'이 안붙어있음
                        answer.append([music_time,music_name])
                        break
                else: # 추가 문자열 검사가 불가, 내가 찾고자 하는 문자열이 전체 악보의 맨 마지막에 있는 경우
                    answer.append([music_time,music_name])
                    break
                        
    if len(answer)==0:
        return '(None)'
    else:
        answer=sorted(answer,key=lambda x: -x[0]) # 조건 일치하는 음악 여러개 일 때, and 순서 유지
        return answer[0][1]
