# Two Pointer Algorithm
import sys
input = sys.stdin.readline

t = int(input()) # 테스트 케이스
for _ in range(t):
    n, K = map(int, input().split())
    arr = list(map(int, input().split())) # 리스트
    arr.sort() # 리스트 오름차순 정렬
    cnt = 0
    MAX = int(1e9)
    l = 0 # 첫번째 index
    r = n - 1 # 마지막 index

    while(l < r):
        # arr[l] + arr[r]과 K의 차가 MAX와 같으면
        if (abs(arr[l] + arr[r] - K) == MAX):
            # 조합의 수 1 추가
            cnt += 1
        # arr[l] + arr[r]과 K의 차가 MAX값보다 작으면
        elif (abs(arr[l] + arr[r] - K) < MAX):
            # MAX값 갱신, cnt = 1
            MAX = abs(arr[l] + arr[r] - K)
            cnt = 1
        # arr[l] + arr[r]과 K의 차가 0보다 작으면
        if ((arr[l] + arr[r] - K) < 0):
            # l을 오른쪽으로 한 칸 이동
            l += 1
        else: # 그렇지 않으면
            # r을 왼쪽으로 한 칸 이동
            r -= 1
    print(cnt)
