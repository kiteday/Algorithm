import sys
input = sys.stdin.readline # 여러 줄 입력받음

# 자신과 놀아준 친구 N(1 ≤ N ≤ 1000)명
# 가지고 있는 돈 B(1 ≤ B ≤ 1,000,000,000)원
N, B = map(int,input().split())

# 선물을 줄 수 있는 친구 수
friend = 0 

gift = [] # 선물의 가격 + 배송비(P(i)+S(i)원)
sale = [] # 쿠폰 사용 가격(⌊P(i)/2⌋+S(i)원)

# N개 줄에는 P(i)와 S(i)
for _ in range(N):
    # 선물의 가격은 P(i)원, 배송비는 S(i)원
    P, S = map(int,input().split())
    # 각각의 값 저장
    gift.append(P + S)
    sale.append((P / 2) + S)

gift.sort() # 오름차순으로 정렬
sale.sort()

def use_coupon(c): # 할인가를 적용
    budget = B - sale[c] # 할인가를 적용하여 구매
    total = 1

    if (budget < 0): # 해당 품목 구매하지 못한 경우
        return 0

    for i in range(N):
        # 선물의 가격이 할인가보가 작거나 같거나(구매가능하거나) and
        # 해당 선물이 할인한 것이 아닌 경우
        if (gift[i] <= budget and i != c):
            # 해당 선물을 구매
            budget -= gift[i]
            total += 1

    return total

# 선물을 최대 몇 명에게 보낼 수 있는지 찾기
for i in range(N):
    if (use_coupon(i) > friend):
        friend = use_coupon(i)

print(friend)
