def solution(price, money, count):
    # count가 증가될 때마다 price에 곱을 해준 값과 money의 차
    for i in range(1, count + 1):
        money -= price * i
    # money가 양수이면 0을, 음수면 절댓값을 return
    if (money >= 0):
        return 0
    else:
        return abs(money)
