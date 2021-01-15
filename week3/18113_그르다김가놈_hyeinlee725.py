import sys
Kimbab = sys.stdin.readline #속도 조절용

# 김밥의 개수 N, 꼬다리의 길이 K, 김밥조각의 최소 개수 M
# 1 ≤ N ≤ 106, 1 ≤ K, M ≤ 109, N, K, M은 정수
N, K, M = list(map(int, Kimbab().split()))

# 김밥의 길이 저장할 배열
#(1 ≤ L ≤ 109, L은 정수)
L = []

for i in range(N): # 두 번째 줄부터 김밥의 길이 L이 N개 주어짐
    L.extend(list(map(int, Kimbab().split()))) # L을 배열에 대입

# 이진 탐색을 하기 위한 변수 start, end
start = 1
end = max(L)
P = -1 # 김밥 길이(Pcm)

while start <= end: # 다음과 같은 동안
    mid = (start + end) // 2 # 탐색 범위의 중간 위치
    cnt = 0 # 김밥 개수

    for i in range(N): # 리스트에 김밥의 길이 추가
        if (L[i] >= 2 * K): # 김밥이 2K보다 길면
            cnt += (L[i] - 2 * K) // mid
        elif (L[i] < 2 * K) and (L[i] > K): # 김밥의 길이가 2K보다 작고 K보다 크면
            cnt += (L[i] - K) // mid
    
    if cnt >= M: # 김밥의 개수가 M개보다 크거나 같으면
        P = max(P, mid) # P에 mid와 P값 중 큰 값 저장
        start = mid + 1
        # 찾는 값이 더 크면 중간을 기준으로 오른쪽 값을 대상으로 이동
    else:
        end = mid - 1
        # 찾는 값이 더 작으면 중간을 기준으로 왼쪽 값을 대상으로 이동

print(P) # 김밥 길이 출력
