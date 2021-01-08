# N, K를 리스트로 반환
# N : 동전의 총 종류, K : 가치의 합
N, K = list(map(int, input().split()))

coin = [] # 동전의 가치 저장할 리스트
count = 0 # 최소 필요한 동전 개수 세기

for i in range(N):
    coin_value = int(input()) # coin_value : N 종류 동전 가치
    if coin_value <= K: # K보다 작은 동전 가치 가진 것만 리스트에 추가
        coin.append(coin_value)
        
coin_len = len(coin) # coin 리스트 길이

for j in range(coin_len):
    # 내림차순으로 이동(큰 동전부터 이용해야 최소값을 구할 수 있음)
    count += K // (coin[(coin_len)-j-1]) # 동전값으로 나눈 몫을 카운트해서 더함
    K = K % coin[(coin_len)-j-1] # 남은 돈 갱신

print(count)
