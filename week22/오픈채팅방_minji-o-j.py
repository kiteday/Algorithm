def solution(record):
    user={} #user id:닉네임 딕셔너리
    log=[] #[id, state] ## Enter:0, Leave:1

    for i in record:
        if i[0]=='E': #Enter    
            state,uid,uname=i.split()
            log.append([uid,0]) #상태 추가
            user[uid]=uname
            
            
        elif i[0]=='L': #Leave
            state,uid=i.split()
            log.append([uid,1]) #상태 추가
            
        elif i[0]=='C': #Change
            state,uid,uname=i.split()
            user[uid]=uname #uid에 저장된 이름 변경
    
    #정답 입력
    answer=[]
    for r_id,r_state in log:
        name=user[r_id]
        if r_state==0:
            answer.append(name+"님이 들어왔습니다.")
        elif r_state==1:
            answer.append(name+'님이 나갔습니다.')
    return answer
