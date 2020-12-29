n=int(input()) #몇자리 수인가?

#idea
'''
주의: 0으로 시작할 수 있다임
0으로 시작 -> 나머지에 다 10 더함
1으로 시작 -> 0빼고 다 10더함 ... (반복)

'''

digit=[[]]
single=[1,1,1,1,1,1,1,1,1,1] #한자리 수
digit.append(single) #한자리 오르막 수 개수 추가

result=sum(single) #초기값: 한자리 수

for i in range(2,n+1): #n자리수까지
    count=[0,0,0,0,0,0,0,0,0,0] # i자리에서 오르막 수 count
    for j in range(0,10): #0~9
        for k in range(j,10):# j랑 같거나 큰거에 계속 더해나갈 예정 (ex:2 - 2~9까지)
            count[k]+=digit[i-1][j]
    digit.append(count)
    
    result=sum(count)


print(result%10007)
