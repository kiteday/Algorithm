def solution(record):
    answer = []
    user = dict()
    log = []
    for r in record:
        data = r.split()
        action, user_id = data[0], data[1]
        if (action in ("Enter", "Change")):
            nickname = data[2] # 가상의 닉네임
            user[user_id] = nickname # 저장된 nickname 변경
        if (action in ("Enter", "Leave")):
            log.append((action, user_id)) # user id와 함께 추가

    # 채팅방 메시지 출력
    for action, user_id in log:
        if (action == "Enter"):
            answer.append(user[user_id] + "님이 들어왔습니다.")
        else:
            answer.append(user[user_id] + "님이 나갔습니다.")
    
    return answer
