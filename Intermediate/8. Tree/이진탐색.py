'''
============================================
[입력]s
3
6
8
15

[출력]
#1 4 6
#2 5 2
#3 8 14
============================================
'''

import math

def binary_searching(array, N,stack,array_list):
    try:
        h = int(math.log2(N))
        if 2**h <= N < 2**h + 2**(h-1):
            select_idx = N-2**(h-1)
        else:
            select_idx = 2**h-1
        stack.append(array[select_idx])
        array_list.append(array[:select_idx])
        array_list.append(array[select_idx+1:])
    except:
        stack.append(array.pop())
    return stack, array_list


test_case = int(input())
for t in range(test_case):
    stack = []

    array_list = [[i+1 for i in range(int(input()))]]

    while True:
        try:
            array = array_list.pop(0)
            stack, array_list = binary_searching(array, len(array), stack,array_list)
        except:
            print("#{0} {1} {2}".format(t+1, stack[0], stack[len(stack)//2-1]))
            break