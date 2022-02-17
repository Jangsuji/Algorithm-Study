'''
============================================
[입력]s
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2

[출력]
#1 4
#2 5
#3 7
============================================
'''

test_case = int(input())
data_dict = []

for t in range(test_case):
  area = [[0 for _ in range(10)] for _ in range(10)]

  num_filter = int(input())
  for i in range(num_filter):
    sw,sh,fw,fh,c = map(int, input().split())
    for h in range(10):
      if sh <= h <= fh:
        for w in range(10):
          if sw <= w <= fw:
             area[h][w]+=1

  newlist = [(i,j) for i in range(10) for j in range(10) if area[i][j]>1]
  print("#{0} {1}".format(t+1, len(newlist)))