# [프로그래머스] 프린터
def solution(priorities, location):
    answer = 0
    
    while priorities:
        maxi = max(priorities)
        printing = priorities.pop(0)
        # 중요도가 가장 높은 문서가 가장 앞에 있다면
        if printing >= maxi:
            answer += 1
            # 내가 요청한 문서가 인쇄됐다면
            if location == 0:
                return answer    
        # 중요도가 가장 높지 않다면 맨 뒤로 이동
        else:
            priorities.append(printing)
        
        # 내가 요청한 문서 위치 이동
        location -= 1
        if location < 0:
            location = len(priorities) - 1
    
    return answer
