'''
============================================
[입력]
2
4 4 2
1 2
1 3
2 4
3 4
4 5 2
1 2
1 3
2 4
3 4
2 3

[출력]
#1 1
#2 0
============================================
'''

def searching(S):
  a = [i for i in range(N) if matrix[S][i]==1]
  return a


test_case = int(input())
for t in range(test_case):

        N, E, M = map(int, input().split())

        matrix = [[0 for _ in range(N)] for _ in range(N)]
        mylist = [list(map(int, input().split())) for _ in range(E)]

        for x in mylist:
                matrix[x[0]-1][x[1]-1] = 1

        cnt = 0
        route = [0]
        color = ['R','B','O','Y']

        while True:
                try: 
                        a = searching(route[cnt])
                        route.extend(a)
                        # print(route)
                        cnt+=1
                        if G in route:
                                score = 1
                                break
                except:
                        score = 0
                        break

        print("#{0} {1}".format(t+1,score))