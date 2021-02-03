from collections import deque
n=int(input()) # 단어의 개수
#-----------
'''
맨 앞에서부터 pop: catrtee일 때 c,a 다음에 tree의 t가 빠지지 않고 cat의 t가 빠지면 no가 뜸
동시에 t t인경우 어떤 t를 뺄지 정하는것 어떻게 고려? -> 이러한 상황 있을 때 저장하고 돌아가
---
aa bab babaa-> 오류 -> copy하는데에서 문제 있었음
---
aba aab abaaba->오류-> 모든 같게 되는 지점을 고려
---
메모리초과 -> index로 접근 -> 시간초과 -> pypy3 -> 메모리초과 -->저장 하면 안될듯? 갈아엎자 ㅠ 
---
dp 이용 -> 단어 1에서 i만큼 단어 2에서 j만큼 썼을 때 가능한가 살펴본다. word1길이xword2길이만큼의 배열 필요
'''
def find(word1,word2,make_word,check,num):
    ## 단어 길이
    w1len=len(word1)
    w2len=len(word2)
    
    for i in range(w1len+1):
        for j in range(w2len+1):

            #0: 불가능 1:가능
            if i==j==0:
                check[i][j]=1 # 초기지점 설정

            if i>0 and make_word[i+j-1]==word1[i-1] and check[i-1][j]: #만들고자 하는 단어의 현재 필요한 철자가 현재 word1 인덱스 자리에 있음, 이전 지점에 가능했었음
                check[i][j]=1 #check[i-1][j] 

            if j>0 and make_word[i+j-1]==word2[j-1] and check[i][j-1]: # t t 인경우 체크해야하니까 elif아니고 if임 
                check[i][j]=1 #check[i][j-1]

    if check[w1len][w2len]: #1 이면
        print('Data set %d: yes' %num)

    else: # 0 이면
        print('Data set %d: no' %num)


#---------실행
for i in range(n): #n회 반복
    word1, word2, make_word=map(str,input().split()) #단어 1, 단어 2, 만들 단어 

    check=[[0 for col in range(len(word2)+1)] for row in range(len(word1)+1)] #배열[word1 최대길이+1][word2 최길이+1] (+1은 0부터 필요하므로) 
    #print(check)
    find(word1,word2,make_word,check,i+1)
