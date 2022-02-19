'''
============================================
[입력]
3
4 4
2 3 4 5
4 8 7 6
9 10 15 16
1 2 6 5
5 5
273 415 58 798 251
675 193 494 506 365
479 390 224 334 387
107 402 569 422 183
88 709 994 206 916
10 10
178 778 659 231 274 123 788 16 483 404
36 14 602 74 287 689 730 703 611 339
445 468 126 821 946 212 218 143 999 923
288 792 249 142 996 999 570 757 141 921
98 87 800 892 401 244 661 179 403 985
474 315 694 816 838 525 288 94 609 6
789 433 474 883 927 841 242 233 286 749
7 667 875 986 107 957 887 520 430 649
721 206 65 776 328 807 845 908 382 836
707 811 790 652 805 190 407 257 668 307

[출력]
#1 16 15 10 9 5 6 7 8 4 4
#2 251 798 365 506 494 193 675 387 334 224
#3 404 483 16 788 123 274 231 659 778 178
============================================
'''

test_case = int(input())
for t in range(test_case):

    array_list = []
    N, M = map(int, input().split())
    for i in range(M):
        array_list.append(list(map(int, input().split())))
    linked_array = array_list[0]

    for array in array_list[1:M]:
        for idx, val in enumerate(linked_array):
            if val > array[0]:
                for i in list(reversed(array)):
                    linked_array.insert(idx, i)
                break
            elif idx == len(linked_array) - 1:
                linked_array.extend(array)
                break

    answer = list(reversed(linked_array))[:10]
    a = ' '.join(str(e) for e in answer)
    print("#{0} {1}".format(t+1,a))
