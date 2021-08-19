'''
[프로그래머스] 문자열 압축
정확성: 100.0
'''
def compression(s, cut):
    st = ''
    cnt = 1
    a = s[:cut] # 압축될 문자
    
    for i in range(cut, len(s), cut):
        b = s[i:i + cut]
        # 문자가 반복되면
        if a == b:
            cnt += 1
        # 문자가 반복되지 않으면
        else:
            if cnt > 1:
                st += str(cnt)
            st += a
            cnt = 1
            a = b
            
    # 마지막 반복 문자 + 나머지 문자
    if cnt > 1:
        st += str(cnt)
    st += a
    
    return len(st)

def solution(s):
    answer = []
    
    for i in range(1, len(s) // 2 + 2): # 문자열이 1~3개일 때를 고려하여 +2
        answer.append(compression(s, i))
    
    return min(answer)
