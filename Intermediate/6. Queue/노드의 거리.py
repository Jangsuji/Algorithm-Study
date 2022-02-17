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

-> 미완성
============================================
'''

def BFS(graph,S):
  visited=[0]*V
  queue = []
  queue.append(S)
  dist = []
  while queue:
    t = queue.pop(0)
    if not visited[t]:
      visited[t] = True
    neighbor = list(filter(lambda x: graph[t][x] == 1, range(V)))
    for i in neighbor:
      if not visited[i]:
        dist.append((t,i))
        queue.append(i)
  if 0 in visited:
    dist = None
  return dist


test_case = int(input())
for t in range(test_case):

  V,E = map(int, input().split())
  graph = [[0 for i in range(V)] for i in range(V)]
  for i in range(E):
    s,d = map(int, input().split())
    graph[s-1][d-1] = 1
    graph[d-1][s-1] = 1
  S,G = map(int, input().split())
  S,G = S-1,G-1
  cnt = 0
  dist = BFS(graph,S)

  while True:
    if dist == None:
      break
    a = [i for i in dist if i[1] == G]
    cnt += 1
    G = a[0][0]
    if G == S:
      break
  print("#{0} {1}".format(t+1,cnt))