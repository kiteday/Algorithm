def solution(s):
    # 숫자, 영단어 표
    word_table = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                  'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    answer = ""
    en_word = ""
    for i in s:
        if i.isdigit(): # 숫자인 경우
            answer += i # 리스트에 바로 추가
        elif i.isalpha(): # 알파벳인 경우
            en_word += i # 치환해서 추가
            if en_word in word_table: # word_table에 해당 단어가 있으면
                answer += str(word_table[en_word]) # 숫자로 바꿔서 리스트에 추가
                en_word = "" # 초기화
    return int(answer)
