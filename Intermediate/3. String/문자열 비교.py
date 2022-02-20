'''
============================================
[입력]
5
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
rithm
a pattern matching algorithm
GYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
GYJZXZTIBSDG
TTXGZYJZXZTIBSDGYJZXZTIBSDG



[출력]
#1 1
#2 0
#3 1
============================================
'''

def BruteForce(p,q):
  i = 0
  j = 0
  while j<M and i<N:
    if q[i] != p[j]:
      i = i-j
      j = -1
    i = i+1
    j = j+1
  if j == M: return 1
  else: return 0


test_case = int(input())

for t in range(test_case):
  p = list(input())
  q = list(input())
  M = len(p)
  N = len(q)
  result = BruteForce(p,q)
  print("#{0} {1}".format(t+1,result))

# test_case = int(input())
#
# for t in range(test_case):
  # str2 = list(input())
  # str1 = list(input())
  # r_str2 = list(reversed(str2))
  # len1, len2 = len(str1), len(str2)
  #
  # step = len2-1
  # step2 = len2-1
  # flag = False
  # flag2 = False
  #
  # while True:
  #   if str1[step] == str2[-1]:
  #     while True:
  #       if str1[step] != str2[step2]:
  #         flag2 = True
  #         break
  #       step -= 1
  #       step2 -= 1
  #       if step2 == -1:
  #         flag = True
  #         break
  #     if flag2:
  #       step += len2
  #   elif str1[step] in str2:
  #     step += r_str2.index(str1[step])
  #   else:
  #     step += len2
  #
  #   if flag or step>=len1:
  #     break
  #
  # if flag:
  #   print("#{0} 1".format(t+1))
  # elif step >= len1:
  #   print("#{0} 0".format(t+1))