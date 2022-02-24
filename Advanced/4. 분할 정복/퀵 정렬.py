'''
============================================
[입력]
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8

[출력]
#1 2
#2 6
============================================
'''

def partition(A,l,r):
    p = A[l]
    i = l+1
    j = r
    while i <= j:
        while(i<=j and A[i]<=p) : i+=1
        while(i<=j and A[j]>=p) : j-=1
        if i <= j:
            A[i],A[j] = A[j],A[i]
    A[l],A[j] = A[j],A[l]
    return j

def quickSort(A,l,r):
    if l<r:
        s = partition(A,l,r)
        quickSort(A,l,s-1)
        quickSort(A,s+1,r)
    return A


test_case = int(input())
for t in range(test_case):

    N = int(input())
    target = list(map(int, input().split()))
    a = quickSort(target,0,N-1)
    print("#{0} {1}".format(t + 1, a[N // 2]))


