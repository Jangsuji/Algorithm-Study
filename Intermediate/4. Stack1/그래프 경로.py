'''
============================================
[입력]s
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9

[출력]
#1 1
#2 1
#3 1
============================================
'''

test_case = int(input())

def searching(S):
  a = [i+1 for i in range(V) if matrix[S-1][i]==1]
  return a


for t in range(test_case):

  V, E = map(int, input().split())
  matrix = [[0 for _ in range(V)] for _ in range(V)]
  mylist = [list(map(int, input().split())) for _ in range(E)]

  for x in mylist:
    matrix[x[0]-1][x[1]-1] = 1

  S, G = map(int, input().split())

  cnt = 0
  route = [S]

  while True:
    try:
      a = searching(route[cnt])
      route.extend(a)
      cnt+=1
      if G in route:
        score = 1
        break
    except:
      score = 0
      break

  print("#{0} {1}".format(t+1,score))