# [9024] 두 수의 합
t = int(input()) # 테스트 개수

for i in range(t):
    n, k = map(int,input().split()) # 정수 개수, 정수의 합
    num = list(map(int, input().split())) # 서로 다른 정수 리스트
    mini = 100000000000 # 최소 거리 (k와 두 정수의 차이)
    rst, l, r = 0, 0, n - 1 # 결과
    
    num.sort() # 리스트 정렬
    
    while(l < r):
        s = num[l] + num[r]
        if(k == s): # k와 s가 같으면 다른 수를 넣어도 k와 제일 가까운 값이 나오지 않으니 왼, 오 둘다 이동
            l += 1
            r -= 1
        elif (k < s): # k가 s보다 작으면 오른쪽 숫자가 너무 크다는 의미로 오른쪽만 -1 이동
            r -=1
        else: # k가 s보다 크면 왼쪽 숫자가 너무 작다는 의미로 왼쪽 +1
            l += 1
        
        if(abs(k - s) < mini): # k와의 거리가 최소 거리보다 더 작은 경우
            mini = abs(k - s)
            rst = 1
        elif(abs(k - s) == mini): # 전과 같은 최소거리라면 
            rst += 1
                
    print(rst)