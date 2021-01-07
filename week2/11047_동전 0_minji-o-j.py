strr=input().split()
n=int(strr[0]) # 동전의 종류
k=int(strr[1]) # 동전 가치의 합
coin_list=[] # 동전 가치가 저장될 배열
coin_cnt=0  #코인 개수 count용

for i in range(n): # 동전 가치는 오름차순
    coin_list.append(int(input()))
    
coin_list=coin_list[::-1] # 역순(큰 순서)으로 바꿈
#print(coin_list)

for j in coin_list:
    count=k//j  # 동전 가치 합 / coin list의 coin(큰 순서대로 계산)
    coin_cnt+=count # 몫 더함
    k-=count*j # 계산해야 할 남은 돈 k 갱신
    
    if k==0:
        break
    
print(coin_cnt)