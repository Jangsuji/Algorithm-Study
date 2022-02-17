'''
============================================
[입력]
3
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
#1 8
#2 14
#3 9
============================================
'''

def queen_check(mask):
  flag = False
  cnt = 0
  for q in mask:
    if sum(q)>0:
      cnt+=1
  if cnt==N:
    flag = "on"
  return flag


test_case = int(input())
for t in range(test_case):

  array_list = []
  N = int(input())
  for i in range(N):
    array_list.append(list(map(int, input().split())))
  mask1 = [[0]*N for _ in range(N)]
  mask2 = [[0]*N for _ in range(N)]
  candidate = []
  results = []

  for num in range(1,11):
    for i in range(N):
      for j in range(N):
        if array_list[i][j] == num:
          mask1[i][j] = 1
          mask2[j][i] = 1
          candidate.append((i,j))
      flag1 = queen_check(mask1)
      flag2 = queen_check(mask2)
    if flag1 and flag2:
      break

  re = candidate[:]

  i = 0
  j = 0
  while True:
    select = candidate.pop(0)
    results.append(select)
    while True:
      try:
        if candidate[j][0] == select[0]:
          candidate.pop(j)
          j-=1
        elif candidate[j][1] == select[1]:
          candidate.pop(j)
          j-=1
        j+=1
      except:
        if j == len(candidate):
          j = 0
          break
    if len(results) == N:
      a = [array_list[i][j] for (i,j) in results]
      print("#{0} {1}".format(t+1,sum(a)))
      break
    elif len(results)+len(candidate)<N:
      re.pop(0)
      candidate = re
      results = []

