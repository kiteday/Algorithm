import sys #종료용

n=int(input()) # 스타트링크 타워의 층수: 10^n, 0 ~ (10^n)-1층
tower=[] #전체 모양 저장

#-------------------------------------
## 전체 입력
for i in range(5): #숫자 길이: 5
    inputline=list(input()) #문자열 하나씩 끊어서 리스트로 바꾸기 
    tower.append(inputline)

#-------------------------------------
## 숫자가 맞는가 확인하는 함수
def checknum(num):
    # 실제 수에는 .인데 들어온 수에서 #이면 다른 숫자임
    # 실제 수에서 . 인 위치만 0/1/2로 표시
    
    n0=[[],[1],[1],[1],[]]
    n1=[[0,1],[0,1],[0,1],[0,1],[0,1]]
    n2=[[],[0,1],[],[1,2],[]]
    n3=[[],[0,1],[],[0,1],[]]
    n4=[[1],[1],[],[0,1],[0,1]]
    n5=[[],[1,2],[],[0,1],[]]
    n6=[[],[1,2],[],[1],[]]
    n7=[[],[0,1],[0,1],[0,1],[0,1]]
    n8=[[],[1],[],[1],[]]
    n9=[[],[1],[],[0,1],[]]

    ablecheck=[] #가능한 수 집합
    n=[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9] #0~9 수 집합
     
    for t in range(0,10): #0~9까지 검사
        flag=0 #0이면 넣고 -1이면 안넣는다.
        for i in range(5): #숫자는 세로5, 바로 끝내기 위하여 3번 반복 안하고 if문 이용
            #print(t,': ',num[i],n[t][i])
            if num[i][0]=='#' and 0 in n[t][i]: # 들어온 수가 #인데 실제는 .임
                flag=-1
                break 
            elif num[i][1]=='#' and 1 in n[t][i]: # 들어온 수가 #인데 실제는 .임
                flag=-1
                break
            elif num[i][2]=='#' and 2 in n[t][i]: # 들어온 수가 #인데 실제는 .임
                flag=-1
                break

        if flag==0:
            ablecheck.append(t)

    return ablecheck

#-------------------------------------
## 한 층씩 나누어서 확인
ablenum=[] #가능한 숫자 배열 list, [[1번째숫자 가능한숫자],[2~],..[n~]] 이런형태
nh=0 #숫자의 가로길이는 3

for i in range(n):
    num=[]
    for j in range(5): #숫자의 세로길이는 5
        num_hor=[] #가로
        for k in range(nh,nh+3):
            #print(tower[j][k],end='')
            num_hor.append(tower[j][k])
        num.append(num_hor)
        #print('\n')
    
    ## 숫자 하나 끝난상태
    able=checknum(num)
    
    if len(able)==0: #길이 0 이면
        print('-1')
        sys.exit() #종료
        
    ablenum.append(able) #이번 숫자가 가능한 숫자들의 집합 넣음
    nh+=4 # 다음층 넘어갈때 점 추가됨

#-------------------------------------
## 배열 곱 함수
def multiply(arr):
    ans = 1
    for n in arr:
        if n == 0:
            return 0
        ans *= n
    return ans

#-------------------------------------
## 조합 숫자 합 구하는 함수
def combsum(n,ablenum): 
    ablenum.reverse() #작은자리수 먼저 오게 순서 변환
    
    lenlist=[] #ablenum 배열의 각각 길이 저장
    m=1 #전체 조합 개수

    for i in ablenum:
        l=len(i)
        m*=l
        lenlist.append(l)

    s=0 #전체 숫자 합

    
    for j in range(0,n):
        dellenlist=lenlist.copy() #copy해야지 lenlist가 안바뀐다.
        del dellenlist[j] # 등장횟수 계산하기 위해서는 자기 제외한 것의 개수 곱을 구해야한다. 자신번째를 제외함
        s+= sum(ablenum[j])*(10**j)* multiply(dellenlist)  # 배열의 합 * 자릿수 * 등장횟수  
    
    return s/m

#-------------------------------------
'''
조합을 이용하여 모두 구한 배열 이용시 메모리에러 발생
합을 바로 구하는 함수 생성
'''
print(combsum(n,ablenum))

