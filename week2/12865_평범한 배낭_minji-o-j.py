import sys
bag=sys.stdin.readline
n,k=map(int, bag().split()) #n: 물품의 수, k:준서가 버틸 수 있는 무게
w_list=[] # 물건 배열
v_list=[] # 가치 배열
cnt=0

for i in range(n):
    cnt+=1
    w,v=map(int, bag().split()) #w: 각 물건의 무게, v: 해당 물건의 가치
    w_list.append(w)
    v_list.append(v)

#print(w_list,v_list) #저장 확인용


'''
완전탐색을 사용할 경우 시간복잡도가 O(2^n)이라서 비효율적임

Knapsack 이용해서 푸는것이 O(n^2)으로 더 효율적

*Knapsack 개념 참고한 곳
https://velog.io/@nokia/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98CC-%ED%8F%89%EB%B2%94%ED%95%9C-%EB%B0%B0%EB%82%ADKnapsack-Problem
(^위에거에 표 중에 잘못된게 있어서 주의해야함 ㅠ)
https://dheldh77.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B0%EB%82%AD-%EB%AC%B8%EC%A0%9CKnapsack-Problem
'''

def Knapsack(n,k,w,v): #총 물건 수, 가방 최대 무게, weight, value
    #최대 가치 배열
    arr=[[0 for col in range(k+1)]for row in range(n+1)] # 0 초기화된 2차원 배열 만들기, (n+1)*(k+1)size
    
    for p in range(1, n+1):# 물건의 수 1~n, n번째 물건은 무조건 넣는다
        for q in range(1, k+1): #가방의 최대 무게, 1~k
            
            if w[p-1]>q:#이번에 넣을 물건의 무게가 q(가방의 최대 무게)보다 큰 경우
                arr[p][q]=arr[p-1][q] #이전 물건까지의 최대 계산한 값 가져온다
                
            else: # w[p-1]<=q # 가방의 최대 무게가 이번에 넣을 물건 무게보다 큼
                # 이전 물건까지의 최대 계산한 값이 더 클까
                # 아니면 이번에 넣을 물건의 가치+(현재 가방 최대 무게-현재 물건의 무게)의 이전 값이 더 클까?
                # 이번걸 넣고 넣을 수 있는 최대를 넣는다는 의미)
                
                arr[p][q]=max(arr[p-1][q],v[p-1]+arr[p-1][q-w[p-1]])
                
    #print(arr) #오류 수정하기 위하여           
    return arr[n][k] #최대 가치(최대 가치 배열이므로 마지막것 반환하면됨)

print(Knapsack(n,k,w_list,v_list))
