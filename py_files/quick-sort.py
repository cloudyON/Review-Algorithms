# 쉬운 ver

# 입ㄹ겨 : 리스트 a
# 출력 :정렬된 새 리스트

def quick_sort(a):
    n = len(a)
    # 종료 조건: 정렬한 리스트이 자료 개수가 한 개 이하이면 정렬할 필요가 없음.
    if n <= 1:
        return a

    #기준 값을 정하고 기준에 맞춰 그룹을 나누는 과정
    pivot = a[-1] # 편의상 리스트의 마지막 값을 기준으로 정함.
    g1 = [] # 그룹1 : 기준 값보다 작은 값을 담을 리스트
    g2 = [] # 그룹2 : 기준 값보다 큰 값을 담을 리스트
    for i in range(0, n-1): # 마지막 값은 기준 값이므로 제외
        if a[i] < pivot: #기준 값과 비교
            g1.append(a[i]) # 작으면 g1에 추가
        else:
            g2.append(a[i]) #크면 g2에 추가

    """
    각 그룹에 대한 재귀 호출로 퀵 정렬을 한 후
    기준 값과 합쳐 하나의 리스트로 결괏값 반환
    """
    return quick_sort(g1) + [pivot] + quick_sort(g2)

d = [6,8,3,9,10,1,2,4,7,5]
print(quick_sort(d))