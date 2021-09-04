from collections import Counter


def make_str_list(str_):
    # 문자열 배열을 만들어서 반환한다
    str_ = str_.lower()
    str_list = []
    for idx in range(len(str_) - 1):
        check_str = str_[idx:idx + 2]
        if check_str.isalpha():
            str_list.append(check_str)
    return str_list


def solution(str1, str2):
    # 문자열 배열 생성
    str1_list = make_str_list(str1)
    str2_list = make_str_list(str2)

    counter1 = Counter(str1_list)
    counter2 = Counter(str2_list)

    # 교집합 생성
    intersection = list((counter1 & counter2).elements())

    # 합집합 생성
    union = list((counter1 | counter2).elements())

    print(union, intersection)

    # 유사도 계산
    if union:
        jaccard = ((len(intersection) / len(union)) * 65536) // 1
    else:
        jaccard = 65536
    return jaccard
