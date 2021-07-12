n,m=map(int,input().split()) #n:행 m:열
'''
검은색으로 시작한다고 가정하면
01010
10101
01010  1) 짝수번째 세로줄 반전: m//2

00000
11111 2)짝수번째 가로줄 반전: n//2
00000 
'''
k=n//2+m//2
print(k)
#세로줄
for i in range(2,m+1,2): #가로 개수만큼
    print(1,i,n,i)
    
#가로
for i in range(2,n+1,2): #세로 개수만
    print(i,1,i,m)



