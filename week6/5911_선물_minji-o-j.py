n,b=map(int,input().split()) #n: 친구 명수, b: 시흠이가 가진 돈
gift=[] #선물 가격 저장용
f_count=0 #선물 줄 수 있는 친구 명수

for _ in range(n):
    cost, shipping=map(int,input().split())
    gift.append([cost+shipping,(cost/2)+shipping]) #두개의 합, 할인가 저장

gift.sort() #정렬
#print(gift) #출력 확인용

'''
정렬: 선물 가격 큰 순->할인가 작은 순
우선 두개의 합 작은 것부터 넣고 넘치는 시점에 할인가 적용한것 중 가장 작은 것 넣는다. ->틀림
>>반례 존재: 2 1506/1000 2/4 1000
---
할인가를 먼저 적용한 후 가능한 모든 경우의수를 고려해본다.
sale할 품목 선택->나머지 개수 세서 count->최댓값 선택 

'''

def find_best(n,b,sale,gift): #sale번째에 할인가를 적용한다.
    total=0
    money=b-gift[sale][1] #sale번째의 항목을 할인가격으로 먼저 구매
    
    if money<0: #선택된 할인 품목 구매 못함
        return total

    total+=1 #할인 품목 구매 했음
    
    for i in range(n): #할인 구매 이후 *정렬된 배열*에서 탐색
        if gift[i][0]<=money and i!=sale: # 구매 가능, 할인항목 아닐 때
            money-=gift[i][0] # 구매
            total+=1
            
    return total


for i in range(n): #최댓값 찾기 
    fb=find_best(n,b,i,gift)
    if fb>f_count:
        f_count=fb #갱신
        
print(f_count)
