import sys
sys.setrecursionlimit(10**6)

str1=list(input()) #문자열 1
str2=list(input()) #문자열 2
len1=len(str1) # 문자열 1 길이
len2=len(str2) #문자열 2 길이

dp=[[0 for col in range(len2+1)] for row in range(len1+1)] #len1행 len2열 2차원 배열

##dp table 채우기
for i in range(1,len1+1): #0인 구간 비워놓고 시작해서 1부터 시작함
    for j in range(1,len2+1):

        
        if str1[i-1]==str2[j-1]: #문자가 같을 때, 인덱스 1부터 셀거라서 문자열에서는 -1씩 함
            dp[i][j]=dp[i-1][j-1]+1

        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

'''
for k in range(len2+1):
    print(dp[k])
'''
print(dp[len1][len2])
if dp[len1][len2]==0:
    sys.exit(0)
    
longstr=[] #긴 문자 저장
## 가장 긴 문자열 출력하기 -> 역순으로 따라가다가 same배열과 일치한 것이 있으면 최대 문자열 목록에 저장
def LCS(dp,i,j,longstr):
    if dp[i][j]==0:
        return
    
    '''
    #3퍼에서 틀리는 코드 ㅠ 반레 뭔지 모르겠어 혹시아는사람~~?
    if dp[i-1][j]==dp[i][j-1]:
        if dp[i][j]>dp[i-1][j-1]: #조건없으면 ABBBB BAAAA에서 B 4번나옴
            longstr.append((i,j)) #숫자가 줄어들었을 때 같은 것 만난 것으로 판단.
        return LCS(dp,i-1,j-1,longstr)

    
    elif dp[i-1][j]>dp[i][j-1]:
        return LCS(dp,i-1,j,longstr) 

    else:
        return LCS(dp,i,j-1,longstr) 
    '''
    
    if dp[i-1][j]==dp[i][j]:
        return LCS(dp,i-1,j,longstr)
    
    elif dp[i][j-1]==dp[i][j]:
        return LCS(dp,i,j-1,longstr)
    
    else:
        longstr.append((i,j))
        return LCS(dp,i-1,j-1,longstr)
LCS(dp,len1,len2,longstr)    

longstr.reverse() #역순으로 뒤집기


for idx1,idx2 in longstr:
    print(str1[idx1-1],end='')
