'''
============================================
[입력]
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX

[출력]
#1 1
#2 4
#3 11
============================================
'''

test_case = int(input())

def removal(data_str):
  flag = 0
  my_str = list(data_str)
  for i in range(len(data_str)):
    if data_str[i-1] == data_str[i] and len(data_str)!=1:
      try:
        del my_str[i-1]
        del my_str[i-1]
        flag = 1
        break
      except:
        flag = 0

  my_str = ''.join(str(e) for e in my_str)
  return my_str, flag


for t in range(test_case):
  data_str = input()
  flag='true'
  while flag:
    data_str, flag = removal(data_str)
  print("#{0} {1}".format(t+1,len(data_str)))