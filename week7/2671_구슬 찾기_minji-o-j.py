n,m=map(int,input().split()) #n: 구슬의 개수, m: 저울에 올려 본 쌍의 개수
'''
자신보다 작은(가벼운)구슬, 큰(무거운) 구슬을 체크한다.
체크했을 때 개수가 (n+1)/2 보다 크거나 같으면 가운데가 될 수 없는 것으로 count한다. (n은 홀수임)
'''
marble_big=[[] for col in range(n+1)] # 자기보다 큰거 저장하는 list, 0번 비워놓을거라서 n+1 함
marble_small=[[] for col in range(n+1)] # 자기보다 작은거 저장하는 list
marble_list=[] #구슬 list, 정렬 위해서 저장

for _ in range(m):
    a,b=map(int,input().split())

    ## 일단 이번에 저울에 올린 것 넣는다.
    marble_big[b].append(a) # 자신보다 큰 것 저장
    marble_small[a].append(b) #자신보다 작은 것 저장

    ## 자신(b)보다 큰 것 목록에 a를 추가 했으므로 b보다 작은 수들의 큰 것 저장하는 목록들에도 a를 추가해야함
    for i in marble_small[b]: #b보다 작은 수 목록 저장 리스트에서
        marble_big[i].append(a)

        ## a>b이므로 a보다 큰 것들은 b보다 작은 수들에게도 크다
        marble_big[i].extend(marble_big[a])

    ## 자신(b)보다 큰 수인 a보다, 큰 수를 b에 추가
    marble_big[b].extend(marble_big[a])
    
    ## 자신(a)보다 작은 것 목록에 b를 추가했으므로 a보다 큰 수들의 작은것 저장하는 목록에도 b를 추가해야함.
    for j in marble_big[a]: #a보다 큰 수 목록 저장 리스트에서
        marble_small[j].append(b)

        ## a>b이므로 b보다 작은 것들은 a보다 큰 수들에게도 작다
        marble_small[j].extend(marble_small[b])

    ## 자신(a)보다 작은 수인 b보다, 작은 것을 a에 추가
    marble_small[a].extend(marble_small[b])
    

    ## 중복 제거
    for t in range(1,n+1):
        marble_small[t]=list(set(marble_small[t])) #메모리 초과때문에 저장하면서 중복 제거
        marble_big[t]=list(set(marble_big[t]))


## 가운데 가능한가 체크
cnt=0 #가운데 불가능한 구슬의 개수
check=(n+1)/2 #비교값

for m in range(1,n+1):
    b=len(marble_big[m]) #큰 것
    s=len(marble_small[m]) #작은 것
    
    if b>=check or s>=check:
        cnt+=1
        
print(cnt)
