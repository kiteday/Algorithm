import sys
input_=sys.stdin.readline
n,k,m=map(int,input_().split()) # n: 손질해야 하는 김밥의 개수, k: 꼬다리의 길이, m: 김밥 조각의 최소 개수
gimbap=[] # 유효한 김밥만 담는 배열
min_gb=1 #최소(초기값)
max_gb=0 #시간 줄이기 위하여 김밥 담는 과정에서 계산

## 김밥 담기
for i in range(n):
    g=int(input())#int(input_().split()[0])
    if g>=(2*k): # 꼬다리 두번 자른 것보다 큰 경우
        gimbap.append(g-2*k)
        max_gb=max(max_gb,g-2*k)
        
    elif g>k: # 2k보다는 작지만 k보다 큰 경우
        gimbap.append(g-k)
        max_gb=max(max_gb,g-k)
        
    else: # 김밥 폐기
        continue
        # continue: 다음 루프로 넘김, continue 구문 아래 실행 안함
        # pass: 그냥 실행시킬 코드가 없는 것
        # break: 루프를 빠져나옴
        
    
#print(gimbap) # 출력 test

'''
가장 길게 만들 수 있는 조각의 길이~ 1까지 김밥 조각의 최소 개수를 만족하는지 확인한다.
가장 길게 만들 수 있는 조각: max(gimbap)
가장 빠른 방법: 이분탐색을 통하여 김밥 조각 길이 지정
'''

save=0 #김밥 조각의 최소 개수를 만족하는 최대 김밥 조각 길이 저장용
klen=(min_gb+max_gb)//2

while (min_gb<=max_gb): #종료 조건
    klen=(min_gb+max_gb)//2 # 꼬다리의 값 min, max 중간부터 시작
    kcount=0 #꼬다리 세기
    
    for j in gimbap: #김밥 배열에서
        kcount+=(j//klen) #만들 수 있는 김밥 조각 구함

    if kcount>=m:  #김밥 조각의 최소 개수를 만족하면
        save=max(klen,save) # 현재 최대 김밥 조각 길이 값이 저장된 것보다 크면 현재 값 저장
        min_gb=klen+1 # 갱신 -> 더 큰 방향으로
        
    else: #최소 개수의 만족하지 못하면
        max_gb=klen-1

if save<=0:
    print(-1)
else:
    print(save)
