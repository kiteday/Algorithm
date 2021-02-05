import sys

N, B = map(int, sys.stdin.readline().split())
PS = [] #0번째는 물건값, 1번째는 배송비
result = 0

for i in range(N):
    PS.append(list(map(int, sys.stdin.readline().split())))

# 물건값+배송비 계산한 값이 작은 값부터 오름차순으로 정렬함
def Sorting():
    flag = False
    while not flag:
        flag = True
        for i in range(N-1):
            if sum(PS[i]) > sum(PS[i+1]):
                tmp = PS[i]
                PS[i] = PS[i+1]
                PS[i+1] = tmp
                flag = False

def UsingCoupon(idx):
    #budget: 갖고있던 돈에서 쿠폰 쓴 물건 뺀 예산 저장
    budget = B-((PS[idx][0]/2)+PS[idx][1])
    count = 1 
    
    if budget < 0:
        return -1

    for i in range(N):
        if sum(PS[i]) <= budget and i != idx:
            budget -= sum(PS[i])
            count += 1
    
    return count

    
Sorting()
for i in range(N):
    cnt = UsingCoupon(i)
    if cnt > result:
        result = cnt   

print(result)