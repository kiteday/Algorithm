def solution(s):
    len_s = len(s)  # 입력 문자열의 길이
    save_len = set([])  # 탐색시 길이 줄이는 목적으로 set 사용

    for cut_len in range(1, len_s // 2 + 1):
        new_str = ''
        find_str = s[:cut_len]
        find_count = 1

        # 문자열 내에서 반복 체크
        for check_idx in range(cut_len, len_s, cut_len):
            # 반복됨
            if find_str == s[check_idx:cut_len + check_idx]:
                find_count += 1
            # 반복되지 않음
            else:
                if find_count == 1:
                    new_str += find_str
                else:
                    new_str += str(find_count) + find_str

                # 새로운 문자 탐색
                find_str = s[check_idx:check_idx + cut_len]
                find_count = 1

        # 남은 문자 추가

        if find_count == 1:
            new_str += find_str
        else:
            new_str += str(find_count) + find_str

        save_len.add(len(new_str))

    # 최솟값 출력
    return min(save_len)
