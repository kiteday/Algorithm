n,m=map(int,input().split()) #n: 레슨의 수, m: 블루레이 개수
lesson=list(map(int,input().split())) # 레슨 순서
b_max=sum(lesson) # m이 1개일 수도 있으므로 하나에 다 들어갈 수도 있음
b_min=max(lesson) # 모든 블루레이 크기는 같으므로 1개씩만 넣더라도 가장 긴 레슨이 블루레이 길이가 됨

'''
b_min~b_max까지 이분탐색을 통해서 블루레이에 들어갈 수 있는 곡의 길이를 제한한다

>> 무엇을 제한하는지 떠올리기 어려웠음ㅠ
'''

while(b_min<=b_max):
    mid=(b_min+b_max)//2
    
    cnt_br=0 #블루레이 개수 count
    size_check=0 #size 더해나가기 위함

    i=-1 #반복용
    
    while(i<n-1): #레슨 처음부터 더해나감, i는 0~n-1까지
        i+=1
        if size_check+lesson[i]<=mid: #이번 값을 더했을 때 mid보다 작거나 같으면
            size_check+=lesson[i]
        else: #이번 값을 size에 더한 값이 mid보다 클 경우
            
            i-=1 #이번 값을 다음에 사용해야함
            
            size_check=0 #초기화
            cnt_br+=1 # 개수 증가
            
    if size_check!=0: #마지막에 더한 값이 mid보다 작거나 같아서 체크 안됨
        cnt_br+=1
        
    if cnt_br<=m: #블루레이 개수가 가능한 블루레이 개수 이하면
        if b_max==mid: #갱신 안되는 경우 -> 아래를 mid-1로 갱신해도됨
            break
        
        b_max=mid
    else:
        if b_min==mid: #갱신 안되는 경우 -> 아래를 mid+1로 갱신해도됨
            break
        b_min=mid
        
#    print(b_min,b_max,cnt_br)

print(b_max)
