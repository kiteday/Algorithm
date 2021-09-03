'''
[프로그래머스] 오픈채팅방
정확성: 100.0
합계: 100.0 / 100.0
'''
def solution(record):
    answer = []
    action = [] # 행동한 순서대로 넣기
    user = {} # 유저아이디 : 닉네임
    
    for S in record:
        st = S.split() # 문자열 공백을 기준으로 분할
                
        # 유저 입장
        if st[0] == 'Enter':
            user[st[1]] = st[2] # 유저아이디 : 닉네임
            action.append([st[0], st[1]]) # 행동과 유저아이디 기록
        # 유저 퇴장
        elif st[0] == 'Leave':
            action.append([st[0], st[1]]) # 행동과 유저아이디 기록
        # 유저 닉네임 변경
        elif st[0] == 'Change':
            user[st[1]] = st[2] # 유저아이디 : 닉네임
            
    for play in action:    
        # 유저 입장
        if play[0] == 'Enter':
            answer.append(f"{user[play[1]]}님이 들어왔습니다.")
        # 유저 퇴장
        elif play[0] == 'Leave':
            answer.append(f"{user[play[1]]}님이 나갔습니다.")
            
    return answer