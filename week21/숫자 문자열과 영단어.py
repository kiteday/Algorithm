# [프로그래머스] 숫자 문자열과 영단어
def solution(s):
    num = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    word = ""
    answer = ""
    
    for i in range(len(s)):
        if s[i].isdigit(): # 숫자라면
            answer += s[i]
        elif s[i].isalpha(): # 알파벳이라면
            word += s[i]
            
        if word in num: # 단어하나가 완성되면 num에서 찾을 수 있음
            answer += num[word]
            word = "" # 영단어를 숫자로 바꾼 후 초기화

    return int(answer)