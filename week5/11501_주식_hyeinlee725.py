import sys

# 테스트케이스 수를 나타내는 자연수
T = int(sys.stdin.readline())

def sell_stock(): # 원하는만큼 주식을 파는 함수
    # 리스트의 마지막 요소 값을 우선 최댓값으로 잡아둠
    max_stock = day_stock[-1]

    max_profit = 0 # 각 테스트케이스 별로 최대 이익

    # 리스트 뒤부터 조회(역순으로 검사)
    for i in range(N - 1, -1, -1):
        # 현재 날 별 주가가 현재 최댓값보다 크면
        if day_stock[i] > max_stock:
            # 최댓값을 현재 날 별 주가로 변경
            max_stock = day_stock[i]
        # 현재 날 별 주가가 현재 최댓값보다 작거나 같으면
        else:
            # 현재 최댓값에서 현재 주가를 뺀 값을 최대 이익에 저장
            max_profit += max_stock - day_stock[i]

    return max_profit

for _ in range(T): # 각 테스트케이스 별로
    # 첫 줄에는 날의 수를 나타내는 자연수 N(2 ≤ N ≤ 1,000,000)
    N = int(sys.stdin.readline())
    # 둘째 줄에는 날 별 주가를 나타내는 N개의 자연수
    day_stock = list(map(int,sys.stdin.readline().split()))

    # 각 테스트케이스 별로 최대 이익을 나타내는 정수 하나를 출력
    print(sell_stock()) 
