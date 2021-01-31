import sys

# 첫째 줄에 오븐의 깊이 D와 피자 반죽의 개수 N(1<=D, N<=300,000)
D, N = map(int,input().split())
# 오븐의 최상단부터 시작하여 깊이에 따른 오븐의 지름
oven = list(map(int,input().split()))
# 피자 반죽이 완성되는 순서대로, 그 각각의 지름
pizza = list(map(int,input().split()))

for i in range(0, D - 1):
    # 오븐의 지름을 가장 작은 값으로 바꿈
    # (하단이 상단보다 큰값인 경우에는 사용 못하므로)
    if oven[i] < oven[i + 1]:
        oven[i + 1] = oven[i]

def Pizza_Baking(): # 피자 굽는 함수
    depth = D - 1
    count = 0

    while count < N:
        result = 0 # 마지막 피자 반죽의 위치
        
        # 아래서부터 탐색(오븐 가장 밑(하단)부터 탐색)
        for i in range(depth, -1, -1): # 역순으로 탐색
            # 오븐에 피자가 들어갈 수 있는 경우
            if oven[i] >= pizza[count]:
                # 다음 위치로 이동
                result = i+1
                depth = i-1 # i부터 피자가 존재하므로 다음 피자는 i - 1에 위치
                break

        # 모두 탐색했는데, 피자가 모두 오븐에 들어가지 않는다면 0을 출력
        if result == 0:
            return 0
        count += 1

    return result

print(Pizza_Baking())
