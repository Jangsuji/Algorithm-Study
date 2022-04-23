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


class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
 
def addList(lst, arr):
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new
 
    if lst.head is None:
        lst.head, lst.tail = first, last
    else:
        cur = lst.head
        while cur is not None:
            if cur.data > arr[0]: break
            cur = cur.next
        if cur is None: # 뒤에 # 순서주의
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last
        elif cur.prev is None: # 앞에 
            last.next = lst.head
            lst.head.prev = last
            lst.head = first
        else: # 중간에 추가
            prev = cur.prev
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
    lst.size += len(arr)
 
def printList(lst):  # 연결리스트 출력
    if lst.head is None:
        return
    cur = lst.tail
    cnt = 10
    while cnt: # 역방향
        print(cur.data, end=' ')
        cur = cur.prev
        cnt -= 1
    print()  
 
for tc in range(1,int(input())+1):
    n,m=map(int,input().split())
    arr = list(list(map(int,input().split())) for _ in range(m)) # 2차원배열로 받기
    mylist = LinkedList()
    for i in range(m):
        addList(mylist, arr[i])
    print(f'#{tc}', end=' ')
    printList(mylist)


# ================================================
# test_case = int(input())
# for t in range(test_case):
#
#     array_list = []
#     N, M = map(int, input().split())
#     for i in range(M):
#         array_list.append(list(map(int, input().split())))
#     linked_array = array_list[0]
#
#     for array in array_list[1:M]:
#         for idx, val in enumerate(linked_array):
#             if val > array[0]:
#                 linked_array = linked_array[:idx]+array+linked_array[idx:]
#                 break
#             elif idx == len(linked_array) - 1:
#                 linked_array.extend(array)
#                 break
#
#     answer = list(reversed(linked_array))[:10]
#     a = ' '.join(str(e) for e in answer)
#     print("#{0} {1}".format(t+1,a))

# ================================================

# ================================================
# class Node:
#     def __init__(self,data=None,next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_begining(self, data):
#         node = Node(data, self.head)
#         self.head = node

#     def insert_at_end(self,data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         itr.next = Node(data, None)

#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)

#     def print(self):
#         if self.head is None:
#             print("empty")
#             return
#         itr = self.head
#         llstr = []
#         while itr:
#             llstr.append(int(itr.data))
#             itr = itr.next
#         return llstr

#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count+=1
#             itr = itr.next
#         return count

#     def remove_at(self, index):
#         if index<0 or index>=self.get_length():
#             raise Exception("Invalid index")
#         if index==0:
#             self.head = self.head.next
#             return
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index-1:
#                 pass
#             itr = itr.next
#             count += 1

#     def insert_at(self,index,data):
#         if index<0 or index>self.get_length():
#             raise Exception("Invalid index")
#         if index == 0:
#             self.insert_at_begining(data)
#             return
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index-1:
#                 node = Node(data,itr.next)
#                 itr.next = node
#                 break
#             itr = itr.next
#             count+=1


# test_case = int(input())
# for t in range(test_case):

#     array_list = []
#     N, M = map(int, input().split())
#     for i in range(M):
#         array_list.append(list(map(int, input().split())))

#     ll = LinkedList()
#     ll.insert_values(array_list[0])
#     # ll.print()
#     for array in array_list[1:]:
#         for idx, node in enumerate(ll.print()):
#             if array[0]<node:
#                 for i in range(M):
#                     ll.insert_at(idx,array[M-1-i])
#                 break
#             if idx == M-1:
#                 for i in range(M):
#                     ll.insert_at_end(array[i])
#         # a = ll.print()
#     result = ll.print()
#     answer = list(reversed(result))[:10]
#     a = ' '.join(str(e) for e in answer)
#     print("#{0} {1}".format(t+1,a))
# ================================================