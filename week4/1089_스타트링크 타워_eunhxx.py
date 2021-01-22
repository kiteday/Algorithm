'''
입력받은 문자열 ('#','.')을 숫자로 바꿔 저장
idea1) #은 1로, .은 0으로 표현
idea2) 자리별로 숫자로 표현 (다이얼패드처럼) --> 이걸로

하나의 숫자 당 규격(크기) 가로3, 세로5로 나타남
숫자별로 지정해둔 numset과의 부분집합으로 비교할수 있음
-> 입력 문자열을 숫자로 바꿔 저장할 때 set형태로 저장해야 함

<순서> (반복문 헷갈림..)
입력받을 문자열은 언제나 5줄
한 줄당 문자열의 길이는 N에따라 달라짐 (4N-1)
숫자를 읽어 저장하기 위해서는 한 줄에서 3칸읽고/한칸띄고/세칸읽고 ... (0,4,8)

시도1) pos에 가능한 층번호가 모두 저장되면 모든 수의 조합을 구함 --> 메모리초과
시도2) 자리수별로 평균 구한다음에 한번에 더함 --> 성공
'''

import sys

N = int(sys.stdin.readline())
temp = []
pos = [[] for _ in range(N)] #가능한 층 번호 저장할 리스트
numset = [frozenset() for _ in range(10)] #frozenset은 변경이 불가능함

# 0~9 각숫자별로 그 자리(다이얼로그 자리)에 해당하는 숫자 저장
numset[0] = {0,1,2,3,5,6,8,9,11,12,13,14}
numset[1] = {2,5,8,11,14}
numset[2] = {0,1,2,5,6,7,8,9,12,13,14}
numset[3] = {0,1,2,5,6,7,8,11,12,13,14}
numset[4] = {0,2,3,5,6,7,8,11,14}
numset[5] = {0,1,2,3,6,7,8,11,12,13,14}
numset[6] = {0,1,2,3,6,7,8,9,11,12,13,14}
numset[7] = {0,1,2,5,8,11,14}
numset[8] = {0,1,2,3,5,6,7,8,9,11,12,13,14}
numset[9] = {0,1,2,3,5,6,7,8,11,12,13,14}

#입력받은 문자열(기호)를 숫자로 변경하여 저장하는 함수
def MarkToNum(idx, k):
    board = set() #숫자로 변경되어 나타난 집합 저장용
    for i in range(5): 
        for j in range(3):
            if temp[i][j+idx] == '#':
                board.add(3*i+j)
                
    # 모두 '.'만 있는 경우 모든 층을 표현할 수 있으므로 따로 계산            
    for i in range(10):
        #부분집합 확인 후, 맞으면 pos(가능한 층번호 저장할 리스트)에 넣음
        if board.issubset(numset[i]) == True:
            pos[k].append(i)


# 가능한 모든 층번호의 평균 구하는 함수
def getAverage():
    rev = pos[::-1] #일의 자리부터 오도록 뒤집어서 저장
    s = 0 #전체 평균 저장할 변수
    
    for i in range(N):
        total = 0 #자릿수별 합 저장할 변수
        k = 10**i
        for j in rev[i]:
            total += (j*k)           
        s += total / len(rev[i])

    return s


# step1) 문자열 전체 입력받아서 temp에 저장함
for i in range(5):
    temp.append(list(sys.stdin.readline().rstrip()))
    
# step2) 입력받는 숫자는 N개니까 N번 반복
for i in range(N):
    idx = 4*i # 0~2, 4~6, 8~10 ... 이런식으로 시작인덱스의 값이 4배수임
    MarkToNum(idx, i) # N번동안 기호->숫자로 바꾸는 함수 호출

# 가능한 층번호가 하나라도 없는경우 -1출력하고 프로세스 종료해버림
for i in range(N):
    if len(pos[i]) == 0:
        print(-1)
        sys.exit()


print(getAverage())