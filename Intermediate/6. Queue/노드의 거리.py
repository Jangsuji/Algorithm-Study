'''
============================================
[입력]
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
1 5
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
#1 2
#2 4
#3 3
============================================
'''

def BFS(graph,S):
  visited=[0]*V
  queue = []
  queue.append(S)
  dist = []
  while queue:
    t = queue.pop(0)
    if not visited[t-1]:
      visited[t-1] = True
    neighbor = list(filter(lambda x: graph[t][x] == 1, range(V+1)))
    for i in neighbor:
      if not visited[i-1]:
        dist.append((t,i))
        queue.append(i)
  return dist


test_case = int(input())
for t in range(test_case):

  V,E = map(int, input().split())
  graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
  for i in range(E):
    s,d = map(int, input().split())
    graph[s][d] = 1
    graph[d][s] = 1
  S,G = map(int, input().split())
  # S,G = S-1,G-1
  cnt = 0
  dist = BFS(graph,S)

  while True:
    try:
      a = [i for i in dist if i[1] == G]
      cnt += 1
      G = a[0][0]
      if G == S:
        print("#{0} {1}".format(t+1,cnt))
        break
    except:
      print("#{0} 0".format(t + 1, cnt))
      break


# ======================================================

# import math
#
# test_case = int(input())
#
# def searching(S):
#   a = [i+1 for i in range(V) if matrix[S-1][i]==1]
#   return a
#
#
# for t in range(test_case):
#
#   V, E = map(int, input().split())
#   matrix = [[0 for _ in range(V)] for _ in range(V)]
#   mylist = [list(map(int, input().split())) for _ in range(E)]
#
#   for x in mylist:
#     matrix[x[0]-1][x[1]-1] = 1
#     matrix[x[1] - 1][x[0] - 1] = 1
#
#   S, G = map(int, input().split())
#
#   cnt = 0
#   route = [S]
#   result = []
#
#   while True:
#     try:
#       a = searching(route[cnt])
#       route.extend(a)
#       result.append(a)
#       cnt+=1
#       if G in route:
#         score = 1
#         break
#     except:
#       score = 0
#       break
#   print(route)
#   print(int(math.log2(len(route)))+1)
  # print("#{0} {1}".format(t+1,score))