'''
============================================
[입력]
3
3 3
1 2 3
2 3 4
3 5
1 3 5
2 4 6 8 10
5 5
1 3 5 7 9
1 2 3 4 5

[출력]
#1 2
#2 0
#3 3
============================================
'''

# def binarySearch2(a b,low,high,key):
#     if low>high:
#         return -1
#     else:
#         middle = (low+high)//2
#         if key ==a[middle]:
#             return middle
#         elif key < a[middle]:
#             return binarySearch2(a,low,middle-1,key)
#         else:
#             return binarySearch2(a,middle+1,high,key)


def binarySearch(a,key):
    start = 0
    end = len(a) - 1
    select = "leftright"
    while start <= end:
        middle = start + (end-start)//2
        if key == a[middle]:
            return middle
        elif key < a[middle] and "right" in select:
            end = middle -1
            select = "left"
        elif a[middle] < key and "left" in select:
            start = middle +1
            select = "right"
        else:
            return -1
    return -1



test_case = int(input())
for t in range(test_case):

    N,M = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0

    for i in B:
        result = binarySearch(A, i)
        if result == -1:
            cnt +=1
    print("#{0} {1}".format(t+1, M-cnt))


