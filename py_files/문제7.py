def solution(stones):
    cnt = 0
    current = 0
    n = len(stones)
    while (current < n):
        current += stones[current]
        print(current)
        cnt += 1
    return cnt

stones1 = [2,5,1,3,2,1]
ret = solution(stones1)
print("solution 함수의 반환 값은", ret, "입니다.")