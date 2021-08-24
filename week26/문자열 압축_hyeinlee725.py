def solution(s):
    # 나눈 문자열의 길이를 담는 list
    length = []
    # 문자열 길이가 1이면 항상 1을 return
    if len(s) == 1:
        return 1
    # range : 나눌 수 있는 최대 길이가 문자열 s의 반
    for cut in range(1, (len(s) // 2) + 1):
        # 문자열 저장
        answer = ""
        # 문자열이 연속으로 반복되는지 확인
        cnt = 1
        # 초기값 설정 - 압축할 문자
        ini_st = s[:cut]
        for i in range(cut, len(s), cut):
            # 다음으로 cut한 값과 같은 경우
            if (ini_st == s[i:cut + i]):
                cnt += 1 # cnt + 1
            else: # 다른 경우
                if (cnt == 1): # cnt가 1이면
                    answer += ini_st # 문자열 저장
                else: # 1이 아니면
                    answer += str(cnt) + ini_st # 숫자와 ini_st에 저장된 값을 저장
                ini_st = s[i:i + cut] # ini)st값 변경
                cnt = 1 # 초기화
        if (cnt == 1): # else로 끝난 경우에만 저장되므로 반복해줌
            answer += ini_st
        else:
            answer += str(cnt) + ini_st
        length.append(len(answer))
    return min(length) # 최소값 return
