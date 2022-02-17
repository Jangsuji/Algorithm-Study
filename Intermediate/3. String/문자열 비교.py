'''
============================================
[입력]
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW

[출력]
#1 1
#2 0
#3 1

-> 8개 맞음 예외 case 2개 존재
-> 제한시간 초과는 아님
============================================
'''

test_case = int(input())    # a pattern matching algorithm

for t in range(test_case):
  str2 = list(input())
  str1 = list(input())
  r_str2 = list(reversed(str2))
  len1, len2 = len(str1), len(str2)

  step = len2-1
  step2 = len2-1
  flag = False
  flag2 = False
  cnt = 0

  while True:
    if str1[step] == str2[-1]:
      cnt = 1
      while True:
        # print(step, step2)
        if str1[step] != str2[step2]:# or step2==0:
          flag2 = True
          break
        step -= 1
        step2 -= 1
        cnt += 1
        if step2 == -1:
          flag = True
          break
      if flag2:
        step += cnt+len2
    elif str1[step] in str2:
      step += r_str2.index(str1[step])
    else:
      step += len2

    if flag or step>=len1:
      break

  if flag:
    print("#{0} 1".format(t+1))
  elif step >= len1:
    print("#{0} 0".format(t+1))