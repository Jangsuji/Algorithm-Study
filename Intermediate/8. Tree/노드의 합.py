'''
============================================
[입력]
3
5 3 2
4 1
5 2
3 3
10 5 2
8 42
9 468
10 335
6 501
7 170
17 9 4
16 479
17 359
9 963
10 465
11 706
12 146
13 282
14 828
15 962

[출력]
#1 3
#2 845
#3 1801
============================================
'''

test_case = int(input())
for t in range(test_case):

  array_list = []
  N, M, K = map(int, input().split())
  data_list = list(map(int, input().split()))
  i = M

  for _ in range(K):
    if i == len(data_list):
      data_list.insert(i, data_list[i - 1] + data_list[0])
      i = M - 1
    else:
      data_list.insert(i, data_list[i - 1] + data_list[i])
      i += M
      if i > len(data_list):
        i -= len(data_list)

  answer = list(reversed(data_list))[:10]
  print("#{0}".format(t + 1), end=" ")

  for i, num in enumerate(answer):
    if i == len(answer) - 1:
      print("{0}".format(num))
    else:
      print("{0} ".format(num), end="")