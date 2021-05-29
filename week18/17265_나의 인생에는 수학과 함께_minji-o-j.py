import itertools
n=int(input()) #n: 지도의 크기, n= 3 or 5
map_=[] #지도 담을 배열
for _ in range(n):
    map_.append(list(input().split(' ')))
#print(map_)
    
# 5번일때 -> 오른쪽으로 4번, 아래로 4번 가야함
# 3번일때 -> 2회, 2회
# 조합: 총 70, 6가지 가능

if n==3: #++--
    c_list=((0,1),(0,1),(1,0),(1,0))
    case=list(set((itertools.permutations(c_list,4)))) #가능한 조합 개수, set으로 중복 없애고->list로 변경
    max_=None
    min_=None
    
    
    for i in case: #case 이동
        row,column=0,0
        initnum=int(map_[row][column]) #계산하는 값
        operator='/' #초기: 없는 연산자로 설정함
        
        for j in i: #case 내에서 숫자 계산
            row+=j[0]
            column+=j[1] #위치 이동
            
            try:
                #숫자로 바꾸기 시도, 성공하면 숫자임
                map_[row][column]=int(map_[row][column])
                
                
                if operator=='+':
                    initnum=initnum+map_[row][column]
                    
                elif operator=='-':
                    initnum=initnum-map_[row][column]
                    
                else: #'*'
                    initnum=initnum*map_[row][column]
                    
            except: #부호임
                operator=map_[row][column]

        #case 끝, 검사
        if min_==None:
            min_=initnum
        if max_==None:
            max_=initnum
            
        max_=max(max_,initnum)
        min_=min(min_,initnum)
                
else: #n==5, ++++----
    c_list=((0,1),(0,1),(0,1),(0,1),(1,0),(1,0),(1,0),(1,0))
    case=list(set((itertools.permutations(c_list,8)))) #가능한 조합 개수, set으로 중복 없애고->list로 변경
    max_=None
    min_=None
    
    
    for i in case: #case 이동
        row,column=0,0
        initnum=int(map_[row][column]) #계산하는 값
        operator='/' #초기: 없는 연산자로 설정함
        
        for j in i: #case 내에서 숫자 계산
            row+=j[0]
            column+=j[1] #위치 이동
            
            try:
                #숫자로 바꾸기 시도, 성공하면 숫자임
                map_[row][column]=int(map_[row][column])
                
                
                if operator=='+':
                    initnum=initnum+map_[row][column]
                    
                elif operator=='-':
                    initnum=initnum-map_[row][column]
                    
                else: #'*'
                    initnum=initnum*map_[row][column]
                    
            except: #부호임
                operator=map_[row][column]

        #case 끝, 검사
        if min_==None:
            min_=initnum
        if max_==None:
            max_=initnum
            
        max_=max(max_,initnum)
        min_=min(min_,initnum)

print(max_,min_)
