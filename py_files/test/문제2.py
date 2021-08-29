def func_a(scores):
    answer = 0
    if scores[0] <= 2:
        answer += 1
    if scores[1] <= 2:
        answer += 1
    if scores[2] <= 1:
        answer += 1

    return answer

def func_b(scores):
    answer = 0
    if scores[0] > 2:
        answer += 1
    if scores[1] > 2:
        answer > 1
    if scores[2] > 1:
        answer += 1

    return answer

def func_c(passed, non_passed):
    return (passed == 3 and non_passed == 0)

def solution(scores):
    answer = 0
    for my_score in scores:
        passed = func_a(my_score)
        non_passed = func_b(my_score)
        answer += func_c(passed, non_passed)
    return answer

scores1 = [[1, 3, 2], [1, 2, 1]]
ret1 = solution(scores1)

print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [[4, 1, 1], [2, 1, 1], [1, 1, 1], [3, 2, 2], [1, 2, 1], [2, 2, 1]]
ret2 = solution(scores2)

print("solution 함수의 반환 값은", ret2, "입니다.")

