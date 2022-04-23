'''
============================================
[입력]
4
4
10 3 2 1
10 2 5 1
10 2 5 6
4 10 10 10
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8

[출력]
9
#1 8
#2 14
#3 9
============================================
'''


def dfs(idx, _sum):
    global min_result
    if idx == N:
        if _sum < min_result:
            min_result = _sum
        return
    #가지치기
    if _sum >= min_result:
        return
    for i in range(N):
        #갔던 세로줄은 사용불가하게 바꾸기
        if use_check[i]:
            use_check[i] = False
            dfs(idx+1, _sum + map_list[idx][i])
            use_check[i] = True
 
T = int(input())
for t in range(1, T+1):
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(N)]
    use_check = [True for _ in range(N)]
    min_result = 100
    dfs(0, 0)
    print("#{} {}".format(t, min_result))


# ==========================================

# import itertools

# test_case = int(input())
# for t in range(test_case):

#     N = int(input())
#     array_list = [list(map(int, input().split())) for _ in range(N)]

#     arr = range(N)
#     nPr = itertools.permutations(arr,N)

#     results = []

#     for i in nPr:
#         a = 0
#         for idx,val in enumerate(i):
#             a += array_list[idx][val]
#         results.append(a)
#     print("#{} {}".format(t+1, min(results)))

# ==========================================