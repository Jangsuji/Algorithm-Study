'''
============================================
[입력]
3
3 6
5 15
5 10

[출력]
#1 1
#2 1
#3 0
============================================
'''

arr = [i for i in range(1,13)]
n = len(arr)

test_case = int(input())

for t in range(test_case):
  N, K = map(int, input().split())

  temp2 = []
  cnt = 0
  for i in range(1<<n):
    temp1 = []
    for j in range(n):
      if i&(1<<j):
        temp1.append(arr[j])

    temp2.append(temp1)
  a = [i for i in temp2 if len(i)==N and sum(i)==K]
  print("#{0} {1}".format(t+1, len(a)))