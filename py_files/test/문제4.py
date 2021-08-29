def solution(price, money):
    answer = 0
    plus = 0
    for i in price:
        plus += i
    
    answer = money - plus

    return answer

price1 = [5300, 2100, 1000, 300]
money1 = 10000
ret = solution(price1, money1)

print("solution 함수의 반환 값은", ret, "입니다.")