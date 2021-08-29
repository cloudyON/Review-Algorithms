
def func_a(arr, n):
    ret = []
    for x in arr:
        if x != n:
            ret.append(x)
    return ret

def func_b(a, b):
    if a >= b:
        return a - b
    else:
        return b - a

def func_c(arr):
    ret = -1
    for x in arr:
        if ret < x:
            ret = x
    return ret

def solution(visitor):
    max_first = func_c(visitor)
    visitor_removed = func_a(visitor, max_first)
    max_second = func_c(visitor_removed)
    answer = func_b(max_first, max_second)

    return answer

visitor1 = [4,7,2,9,3]
ret = solution(visitor1)
print("solution 함수의 반환 값은", ret, "입니다.")
