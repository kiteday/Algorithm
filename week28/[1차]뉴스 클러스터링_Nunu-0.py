# [프로그래머스] [1차]뉴스 클러스터링
def solution(str1, str2):
    # 문장을 모두 대문자로 바꾸기
    str1 = str1.upper()
    str2 = str2.upper()
    # 두 글자씩 끊은 집합을 넣을 리스트
    str1_list = []
    str2_list = []
    
    # str1 집합 만들기
    for i in range(len(str1)-1):
        front = str1[i]
        back = str1[i + 1]
        if front.isalpha() and back.isalpha(): # 두 글자 모두 알파벳일때
            str1_list.append(front + back)
    # str2 집합 만들기        
    for i in range(len(str2)-1):
        front = str2[i]
        back = str2[i + 1]
        if front.isalpha() and back.isalpha(): # 두 글자 모두 알파벳일때
            str2_list.append(front + back)
    
    # 교집합
    inter = set(str1_list) & set(str2_list)
    inter_cnt = sum([min(str1_list.count(i), str2_list.count(i)) for i in inter]) # 다중 교집합 개수 
    # 합집합
    union = set(str1_list) | set(str2_list)
    union_cnt = sum([max(str1_list.count(i), str2_list.count(i)) for i in union]) # 다중 합집합 개수

    # 유사도
    if inter_cnt == 0 and union_cnt == 0:
        similarity = 1
    else:
        similarity = inter_cnt / union_cnt
    
    return int(similarity * 65536)
