from collections import Counter
def solution(str1, str2):
    str1_list = [] # 2글자씩 나눠서 저장할 list
    str2_list = []
    for i in range(0, len(str1) - 1):
        # str1 값을 2글자 단위로 쪼개서 두 값이 모두 알파벳이면
        if (str1[i:i + 2].isalpha()):
            # 소문자로 바꿔서 저장
            str1_list.append(str1[i:i + 2].lower())
    for i in range(0, len(str2) - 1):
        # str2 값을 2글자 단위로 쪼개서 두 값이 모두 알파벳이면
        if (str2[i:i + 2].isalpha()):
            # 소문자로 바꿔서 저장
            str2_list.append(str2[i:i + 2].lower())
    # 각 문자열이 몇 개있는지 count해서 교집합과 합집합 구하기
    inter = list((Counter(str1_list) & Counter(str2_list)).elements())
    union = list((Counter(str1_list) | Counter(str2_list)).elements())
    # 모두 공집합일 경우, 1 * 65536 return
    if (len(union) == 0 and len(inter) == 0):
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
