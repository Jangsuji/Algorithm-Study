'''
============================================
[입력]
3
5 3 4
1 2 3 4 5
I 2 7
D 4
C 3 8
5 5 2
15171 7509 20764 13445 10239
C 3 18707
C 1 20250
D 2
D 2
C 0 7158
10 10 8
27454 29662 2491 1819 10118 15441 7357 23618 972 398
D 7
D 1
D 6
I 3 2906
C 1 27121
D 3
D 2
D 1
D 2
C 2 20794

[출력]
#1 5
#2 10239
#3 -1
============================================
'''

def edit(edit_case, data_list):
  if edit_case[0] == 'I' :
    data_list.insert(int(edit_case[1]),int(edit_case[2]))
  elif edit_case[0] == 'C' :
    data_list[int(edit_case[1])] = int(edit_case[2])
  elif edit_case[0] == 'D' :
    data_list.pop(int(edit_case[1]))
  return data_list

test_case = int(input())
for t in range(test_case):

  N,M,L = map(int, input().split())
  data_list = list(map(int, input().split()))
  edit_list = [tuple(input().split()) for _ in range(M)]

  for i in edit_list:
    data_list = edit(i, data_list)

  print("#{0}".format(t+1), end =" ")
  try:
    print(data_list[L])
  except:
    print('-1')