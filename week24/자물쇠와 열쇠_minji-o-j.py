import numpy as np

def solution(key, lock):
    '''
    완전탐색
    1) Key<=Lock
    2) Lock에 Key-1만큼 Padding을 한다(-2로)
    3) key를 lock에 더했을 때 0이 남아있거나, 2가 있으면 continue
    4) 하나라도 성공하는 것이 있으면 바로 True 반환
    '''
    ## numpy 변환 (shape 얻기 위함)
    key=np.array(key)
    lock=np.array(lock)
    
    ## 가로 세로 길이 알아내기
    key_num=key.shape[0]
    lock_num=lock.shape[0]

    ## padding
    lock_pad=lock.copy()
    lock_pad=np.pad(lock, ((key_num-1,key_num-1),(key_num-1,key_num-1)), 'constant', constant_values=-2)
    
    ## 찾기 시작
    answer = False
    for _ in range(4):
        key=np.ndarray.tolist(np.rot90(key)) #배열 회전
        for i in range(lock_num+key_num-1): #lock_pad길이-key길이+1=lock길이+(key길이-1)*2-key길이+1
            for j in range(lock_num+key_num-1):
                lock_now=lock_pad.copy() #복사본
                for k_i in range(key_num):
                    for k_j in range(key_num):
                        lock_now[i+k_i][j+k_j]+=key[k_i][k_j]
                if 0 in lock_now or 2 in lock_now:
                    continue
                else:
                    return True

    return answer
