N=int(input()) #학생의 수
number=[int(input()) for _ in range(N)] #입력받은 수
count=[0 for _ in range(max(number)+1)] #각 수가 몇개씩 들어왔는지 개수 count

#약수 구해서 그에 해당하는 숫자 세놓은거 더해줌
def Divisor(n):
    cnt=0
    for i in range(1, int(n**(1/2))+1):
        if (n%i)==0: #약수인 경우
            cnt += count[i] #count배열에 세놓은거 더해줌
            if (i**2)!=n: #그 약수의 짝 구함
                cnt += count[n//i] #이것도 더해줌
    
    return cnt

#입력받은 수들 중 동일한 수 몇개 들어왔는지 count
for i in range(N):
    count[number[i]] += 1
    
for i in range(N):
    result=Divisor(number[i])
    print(result-1) # -1은 자기 자신도 같이 count된거 뺌
