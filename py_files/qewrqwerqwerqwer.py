# 친구 리스트에서 자신의 모든 친구를 찾는 알고리즘
# 입력 : 친구 관계 그래프 g, 모든 친구를 찾을 자신 start
#출력 : 모든 친구의 이름

def print_all_friends(g, start):
    qu = list()# 기억 장소 1: 앞으로 처리해야 할 사람들을 큐에 저장
    done = set() # 기억 장소 2: 이미 큐에 추가한 사람들을 집합에 기록(중복 방지)

    qu.append(start) # 자신을 큐에 넣고 시작
    done.add(start) # 집합에도 추가

    while qu: # 큐에 처리할 사람이 남아 있는 동안
        p = qu.pop(0) # 큐에서 처리 대상을 한 명 꺼내
        print(p) # 이름을 출력하고
        for x in g[p]: #그의 친구들 중에
            if x not in done: # 아직 큐에 추가된 적이 없는 사람들
                qu.append(x) # 큐에 추가하고
                done.add(x) # 집합에도 추가


fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
	'John': ['Summer', 'Justin'],
	'Justin': ['John', 'Summer', 'Mike', 'May'],
	'Mike': ['Summer', 'Justin'],
	'May': ['Justin', 'Kim'],
	'Kim': ['May'],
	'Tom': ['Jerry'],
	'Jerry': ['Tom']
}

print_all_friends(fr_info, "Summer")
print()
print_all_friends(fr_info, "Jerry")



print("\n-----------\n")
#------------------------------------------------
def PrintAllFriends(g, start):
    qu = list()
    done = set()

    qu.append((start, 0))

    done.add(start)

    while qu:
        (p,d) = qu.pop(0)
        print(p, d)
        for x in g[p]:
            if x not in done:
                qu.append((x, d + 1))
                done.add(x)

fr_info = {
	'Summer': ['John', 'Justin', 'Mike'],
	'John': ['Summer', 'Justin'],
	'Justin': ['John', 'Summer', 'Mike', 'May'],
	'Mike': ['Summer', 'Justin'],
	'May': ['Justin', 'Kim'],
	'Kim': ['May'],
	'Tom': ['Jerry'],
	'Jerry': ['Tom']
}

PrintAllFriends(fr_info, "Summer")
print()
PrintAllFriends(fr_info, "Jerry")
