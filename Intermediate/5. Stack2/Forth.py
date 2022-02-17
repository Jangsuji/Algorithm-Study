'''
============================================
[입력]
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .

[출력]
#1 84
#2 error
#3 168
============================================
'''


test_case = int(input())
for t in range(test_case):
  data_str = input()
  my_str = data_str.split(' ')
  stack = []

  if my_str[-1] != '.':
    print("#{0} error".format(t+1))

  else:
    for char in my_str:

      if char.isdigit():
        stack.append(char)

      elif char == '.':
        result = stack.pop()
        if not stack:
          print("#{0} {1}".format(t+1, result))
        else:
          print("#{0} error".format(t+1))
          break

      else:
        try:
          second = stack.pop()
          first = stack.pop()
          if char == '+':
            calc = int(first)+int(second)
          elif char == '-':
            calc = int(first)-int(second)
          elif char == '*':
            calc = int(first)*int(second)
          elif char == '/':
            calc = int(int(first)/int(second))
          else:
            print("#{0} error".format(t+1))
            break
          stack.append(calc)
        except:
          print("#{0} error".format(t+1))
          break
