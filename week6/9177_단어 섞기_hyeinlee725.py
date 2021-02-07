# 파이썬 모듈 사용 - Queue 이용
from collections import deque
import sys
input = sys.stdin.readline

# 데이터 집합의 개수(1부터 1000까지의 양의 정수)
N = int(input())

def check(word1, word2, new_word): # 단어를 확인하는 함수
    l1 = len(word1) # 첫번째 단어 길이
    l2 = len(word2) # 두번째 단어 길이
    ln = len(new_word) # 세번째 단어 길이

    queue = deque() # deque 선언
    # word1, word2 위치
    queue.append([0, 0])
    ch[0][0] = True

    while (len(queue) != 0):
        a, b = queue.pop()
        c = a + b

        # True : 가능, False : 불가능
        # 각각 길이가 같으면 True
        if (a == l1 and b == l2 and c == ln):
            return True

        # 세 번째 단어가 첫 번째 단어와 두 번째 단어의 합이면 True
        if (word1 + word2 == new_word or word2 + word1 == new_word):
            return True

        # 현재 a의 위치값과 c의 위치값이 같다면
        if (a < l1 and word1[a] == new_word[c]):
            # a + 1을 했을 때 ch 배열이 True인 경우
            if(not ch[a + 1][b]):
                # a의 다음 위치로 이동
                queue.append((a + 1, b))
                ch[a + 1][b] = True

        # 현재 b의 위치값과 c의 위치값이 같다면
        if (b < l2 and word2[b] == new_word[c]):
            # b + 1을 했을 때 ch 배열이 True인 경우
            if (not ch[a][b + 1]):
                # b의 다음 위치로 이동
                queue.append((a, b + 1))
                ch[a][b + 1] = True

    # 위에 해당하지 않는 경우 False 반환
    return False


for i in range(N): # 각 데이터집합에 대해
    # 세 개의 단어로 이루어져 있으며 공백으로 구분
    word1, word2, new_word = map(str,input().split())

    # 단어 check할 배열
    ch = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

    # 만약 첫 번째 단어와 두 번째 단어로 세 번째 단어를 형성할 수 있다면(True라면)
    if (check(word1, word2, new_word)):
        print('Data set %d: yes' %(i+1))
    else: # 아니라면(False라면)
        print('Data set %d: no' %(i+1))
