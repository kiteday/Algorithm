import sys
input = sys.stdin.readline # 여러 줄 입력받음

# 스타트링크 타워 층수 N(N은 9보다 작거나 같은 자연수)
N = int(input())

# 전체 Input 저장(5줄에 걸쳐서 저장)
tower = [input()[:-1] for _ in range(5)]
pos_num = [[]for _ in range(N)] # 가능한 모든 층 번호를 저장할 배열
num = [set() for _ in range(10)] # 숫자 배열 set

# 숫자가 맞는지 확인하는 함수
def check(index, input_num):
    # 숫자 0~9에서 불이 켜져있는 위치 즉, '#'의 위치를 표시해서 각각 배열에 저장
    num[0] = {0, 1, 2, 3, 5, 6, 8, 9, 11, 12, 13, 14}
    num[1] = {2, 5, 8, 11, 14}
    num[2] = {0, 1, 2, 5, 6, 7, 8, 9, 12, 13, 14}
    num[3] = {0, 1, 2, 5, 6, 7, 8, 11, 12, 13, 14}
    num[4] = {0, 2, 3, 5, 6, 7, 8, 11, 14}
    num[5] = {0, 1, 2, 3, 6, 7, 8, 11, 12, 13, 14}
    num[6] = {0, 1, 2, 3, 6, 7, 8, 9, 11, 12, 13, 14}
    num[7] = {0, 1, 2, 5, 8, 11, 14}
    num[8] = {0, 1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13, 14}
    num[9] = {0, 1, 2, 3, 5, 6, 7, 8, 11, 12, 13, 14}

    check_num = set() # 숫자로 만들 집합 저장해서 set
    for c in range(3): # column(3열)
        for r in range(5): # row(5행)
            if tower[r][index + c] == '#': # 해당 위치가 '#'이면
                check_num.add(r * 3 + c) # 해당 위치의 숫자를 더함
                
    for i in range(10): # 총 10개의 수(0 ~ 9)
        # num 배열에 있는 값과 check_num에 있는 값의 교집합이 같으면
        if num[i].intersection(check_num) == check_num:
            # 리스트에 저장
            pos_num[input_num].append(i)

def Cal_Average(): # 평균을 계산하는 함수
    total_floor = 1 # 가능한 층번호 개수
    sum_list = [] # 각각의 숫자와 개수를 저장할 배열

    # 가능한 모든 층 번호에 대하여
    for i, v in enumerate(pos_num): # index와 value값으로 반환(tuple 형태)
        total_floor *= len(v) # 전체 개수 추가 - value 개수만큼 곱함
        
        num = 0 # 각각의 값
        for j in v: # value 안에 있을 때
            num += j # 해당 값을 더함

        # 해당 숫자 배열에 각각의 값 * 자릿수만큼한 값을 저장
        # 총 value가 몇 개 존재하는지 저장
        sum_list.append([num * (10 ** (N - i - 1)), len(v)])
    
    if total_floor == 0: # 가능한 층번호가 하나도 없는 경우
        print(-1) # 가능한 층 번호가 없는 경우 -1을 출력
        return

    else: # 가능한 층번호가 존재하면
        total_sum = 0 # 총합
        for v in sum_list:
            # 각각의 값과 가능한 층번호 개수를 총 value의 개수로 나눈 값을 더한다
            total_sum += v[0] * total_floor // v[1]

    # (전체 합 / 전체 층 개수) 반환
    return (total_sum / total_floor)
    
# 입력받는 N개의 숫자에 대해
for i in range(N):
    index = 4 * i # 시작하는 숫자 index 번호에 따라(0 ~ 2, 4 ~ 7 ...)
    check(index, i) # 숫자가 맞는지 check
    
print(Cal_Average())
