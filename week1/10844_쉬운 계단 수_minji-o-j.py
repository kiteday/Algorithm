n=int(input()) #몇자리 수인가?

#idea
'''
마지막 숫자 개수 배열 만듦
그리고 더해나감

ex) 1자리일 때 6으로 끝나는거 1개-> 2자리일때 5로 끝나는거에 +1, 7로끝나는거에 +1...(반복)
'''

last=[[]] #index 접근 편하게 하기 위하여 0자리수 배열 만듦
start=[0,1,1,1,1,1,1,1,1,1] # 시작: 1자리수 -> 이게왜 계단수인지는 모르겠지만? 일단은
last.append(start) #저장
# print(last)
result=sum(start)

for i in range(2,n+1): #2자리수부터 n자리까지
    count=[0,0,0,0,0,0,0,0,0,0]
    
    for j in range(0,10): #0~9까지 접근
        if j!=0 and j!=9: #양쪽 계산을 위하여 0,9 제외
            count[j]+=last[i-1][j-1] #왼쪽 수
            count[j]+=last[i-1][j+1] #오른쪽 수
            
        elif j==0:
            count[j]+=last[i-1][j+1] #오른쪽 수
            
        else: #j==9
            count[j]+=last[i-1][j-1] #왼쪽 수
            
    last.append(count) #계산된 것 추가
    
    if(i==n):
        #print(last[i])
        result=sum(last[i])


print(result%1000000000)
