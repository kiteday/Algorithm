import math
from collections import Counter

N = int(input())
# 머리에 쓴 숫자
Stu_num = []
# 머리 친 개수(자기 자신은 빼기 위해 -1로 초기화)
cnt = [-1 for _ in range(N)]

# 1번부터 N번까지 각각의 학생이 자신의 머리에 쓴 숫자 입력
for _ in range(N):
    Stu_num.append(int(input()))

# 리스트 원소의 개수 count
count = Counter(Stu_num)

# 약수 구하기
for i in range(N):
    # i번째 학생이 머리에 쓴 숫자
    num = Stu_num[i]
    # 약수 저장 list
    div = []
    # 루트를 이용하여 계산
    for j in range(1, int(math.sqrt(num)) + 1):
        # 나머지가 0이면 약수
        if (num % j == 0):
            div.append(j)
            # 자연수 N의 제곱근까지의 약수를 구하면 그 짝이 되는 약수도 있으므로 추가
            if (j != num // j):
                div.append(num //j)
    # 약수 개수 count(머리 친 개수)
    for d in div:
        cnt[i] += count[d]
# 결과 출력
for res in cnt:
    print(res)
