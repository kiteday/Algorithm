# [프로그래머스] 1주차
def solution(price, money, count):
    amount = 0
    
    for i in range(0, count + 1):
        amount += price * i
    
    if money < amount:
        return amount - money;
    else:
        return 0