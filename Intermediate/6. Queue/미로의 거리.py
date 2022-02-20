'''
============================================
[입력]s
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

[출력]
#1 5
#2 5
#3 0
============================================
'''

def neighbor_serching(mazeArray,index):
  neighbor = []
  if mazeArray[index[0]-1][index[1]] in (0, 2, 3):
    neighbor.append((index[0]-1,index[1]))
  if mazeArray[index[0]+1][index[1]] in (0,2,3) :
    neighbor.append((index[0]+1,index[1]))
  if mazeArray[index[0]][index[1]-1] in (0,2,3) :
    neighbor.append((index[0],index[1]-1))
  if mazeArray[index[0]][index[1]+1] in (0,2,3) :
    neighbor.append((index[0],index[1]+1))
  return neighbor



test_case = int(input())
for t in range(test_case):

  maze_size = int(input())
  mazeArray = [[int(i) for i in list(input())] for _ in range(maze_size)]

  for i in range(maze_size):
    mazeArray[i].insert(0,1)
    mazeArray[i].append(1)
  pad = [1]*(maze_size+2)
  mazeArray.insert(0,pad)
  mazeArray.append(pad)

  for i in range(maze_size+2):
    try:
      start = mazeArray[i].index(2)
      start_index = (i, start)
    except:
        pass
    try:
      end = mazeArray[i].index(3)
      end_index = (i, end)
    except:
      pass

  stack = [start_index]
  index = start_index
  flag = False

  while True:
    neighbor = neighbor_serching(mazeArray, index)
    if not neighbor:
      break

    elif len(neighbor) == 1:
      index = neighbor.pop(0)
      if index == end_index:
        flag = True
        break
      try:
        if index == stack[-2]:
          mazeArray[stack[-1][0]][stack[-1][1]] =1
          stack.pop()
        elif index == end_index:
          flag = True
          break
        else:
          stack.append(index)
      except:
        stack.append(index)

    elif len(neighbor) != 1:
      index = neighbor.pop(0)
      if index == end_index:
        flag = True
        break
      try:
        if index == stack[-2]:
          index = neighbor.pop(0)
          if index == end_index:
            flag = True
            break
          stack.append(index)
        else:
          stack.append(index)
      except:
        stack.append(index)

  if flag:
    print("#{0} {1}".format(t+1, len(stack)-1))
  else:
    print("#{0} 0".format(t+1))