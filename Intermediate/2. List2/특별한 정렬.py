'''
============================================
[입력]
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26

[출력]
#1 10 1 9 2 8 3 7 4 6 5
#2 89 8 85 11 67 16 60 28 49 39
#3 98 3 97 9 88 17 75 18 71 21
============================================
'''


test_case = int(input())


for t in range(test_case):
  num = int(input())
  data_list = list(map(int,input().split()))
  sorted_list = sorted(data_list)
  reversed_list = sorted(data_list, reverse=True)
  a = []
  for i in range(5):
    a.append(reversed_list[i])
    a.append(sorted_list[i])
  w = ' '.join(str(e) for e in a)
  print("#{0} {1}".format(t + 1, w))