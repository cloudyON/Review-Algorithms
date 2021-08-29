# 리스트에서 특정 숫자 찾기 (이분 탐색)
# 입력 : 리스트 a, 찾는 값 : X
# 출력 : 찾으면 그 값의 위치, 찾지 못하면 -1

def binary_search(a,x):
    #탐색할 범위를 저장하는 변수 start, end
    #리스트 전체를 범위로 탐색 시작
    start = 0 # 1
    end = len(a) -1 # 1

    while start <= end: 
        mid = (start + end) // 2 # 1
        if x == a[mid]: # 1
            return mid # 1

        elif x > a[mid]: # 1
            start = mid + 1 # 1

        else: # 1
            end = mid - 1 # 1

    return -1

# d = [1,4,9,16,25,36,49,64,81]
# print(binary_search(d, 36))
# print(binary_search(d, 50))


def recursive(a, x):
    start = 0
    end = len(a) - 1

    if start > end:
        return -1

    mid = (start + end) // 2

    if x == a[mid]:
        return mid

    elif x > a[mid]:
        return recursive(a[(mid+1):], x)

    else :
        return recursive(a[:mid], x)

d = [1,4,9,16,25,36,49,64,81]
print(recursive(d, 36))
print(recursive(d, 50))




# 리스트 r에서 v가 들어가야 할 위치를 돌려주는 함수
def find_ins_idx(r, v):
	# 이미 정렬된 리스트 r의 자료를 앞에서부터 차례로 확인하여
	for i in range(0, len(r)): #r 2len(r)
	
		if v < r[i]: #1
			return i #1
		# 적절한 위치를 못 찾았을 때는
		# v가 r의 모든 자료보다 크다는 뜻이므로 맨 뒤에 삽입
	return len(r)

def ins_sort(a):
	result = [] #1 # 새 리스트를 만들어 정렬된 값을 저장
	while a:   #a(2*len(r)+2) # 기존 리스트에 값이 남아 있는 동안 반복
		value = a.pop(0) 1 # 기존 리스트에서 한 개를 꺼냄
		ins_idx = find_ins_idx(result, value) #2*len(r) # 꺼낸 값이 들어갈 적당한 위치 찾기
		result.insert(ins_idx, value) 1 # 찾은 위치에 값 삽입 (이후 값은 한 개씩 밀려남)
	return result # 1

    # a(2*len(r)+2) + 1 = 2*len(r)a + 2a 1 -> len(r)a


d = [2, 4, 5, 1, 3]
print(ins_sort(d))