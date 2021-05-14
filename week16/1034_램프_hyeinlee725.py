# N : 행의 개수, M : 열의 개수
N, M = map(int, input().split())
# 램프 상태
lamp_table = [input() for _ in range(N)]

# 스위치 누르는 횟수(1,000보다 작거나 같은 자연수 또는 0)
K = int(input())
col_cnt = 0 # 켜져있는 행 개수 count

# 모든 행에 대해 반복
for col in range(N):
    # 꺼진 전구 개수(0인 전구 개수)
    zero_cnt = 0

    # lamp_table[col]의 램프에 대해
    for lamp in lamp_table[col]:
        # 램프가 꺼져있으면, count+1
        if lamp == '0':
            zero_cnt += 1

    # 동일한 열의 개수 count
    cnt_row = 0 # same row
    # 꺼진 전구개수가 K보다 작거나 같다면
    # 만약 N행의 꺼진 전구의 개수와 K가 모두 짝수라면(or 홀수)
    if (zero_cnt <= K and zero_cnt % 2 == K % 2):
        for colu in range(N):
            # 행이 서로 같으면 count+1
            if (lamp_table[col] == lamp_table[colu]):
                cnt_row += 1

    # 켜져있는 행의 값을 최대로 함
    col_cnt = max(col_cnt, cnt_row)

print(col_cnt)
