'''
============================================
[입력]
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())

[출력]
#1 1
#2 1
#3 0
============================================
'''


def push(item):
  s.append(item)

def pop():
  if len(s) ==0:
    return
  else:
    return s.pop(-1)


test_case = int(input())

for t in range(test_case):
  s = []
  data_string = input()
  characters = "[]{}()"
  cnt = 0

  string = ''.join( x for x in data_string if x in characters)

  if len(string)%2 != 0:
    print("#{0} 0".format(t+1))
  else:
    for i in string:
      if i in '[{(':
        push(i)
        cnt +=1
      else:
        if (s[-1]=='[' and i==']') or (s[-1]=='{' and i=='}') or (s[-1]=='(' and i==')'):
          pop()
          cnt +=1
        else:
          print("#{0} 0".format(t+1))
          break

    if len(string) == cnt:
      print("#{0} 1".format(t+1))