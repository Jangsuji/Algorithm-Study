'''
============================================
[입력]
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8

[출력]
#1 2 0
#2 6 6
============================================
'''

def merge(left,right):
    result = []
    if left[-1] > right[-1]:
        cnt.append(1)
    while len(left)>0 and len(right)>0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left)>0:
        result.extend(left)
    if len(right)>0:
        result.extend(right)
    return result

def merge_sort(m):
    if len(m) <= 1:
        return m
    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)



test_case = int(input())
for t in range(test_case):

    N = int(input())
    target = list(map(int, input().split()))
    cnt = []
    a = merge_sort(target)
    print("#{0} {1} {2}".format(t+1, a[N//2], sum(cnt)))








