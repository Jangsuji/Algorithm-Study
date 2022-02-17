'''
============================================
[입력]
3
6 3 3
6 2 4 9 1 5
5 3 5
958 386 329 169 778
10 4 10
158 606 636 941 686 774 302 375 954 668

[출력]
#1 5 6 1 9 13 4 2 8 6
#2 1736 2514 778 169 667 498 329 715 386 958
#3 826 1494 668 954 375 1052 677 302 774 2234
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