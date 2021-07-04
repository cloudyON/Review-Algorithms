# 삽입 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)

def InsSort(a):
    n = len(a)
    for i in range(1,n): # 1부터 n-1까지
        #i번재 위치에 잇는 값을 key에 저장
        key = a[i]
        # j를 i 바로 왼족 위치에 저장
        j = i - 1
        # 리스트의 j번 위치에 잇는 값과 key를 비교해 key가 삽입될 적절한 위치를 찾음
        while j >= 0 and a[j] > key:
            # 삽입될 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            a[j + 1] = a[j]
            j -= 1
        a[j+1] = key # 찾은 삽입 위치에 key를 저장

d = [2,4,5,1,3]
InsSort(d)
print(d)