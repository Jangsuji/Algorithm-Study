'''
============================================
[입력]s
3
10 10
GOFFAKWFSM
OYECRSLDLQ
UJAJQVSYYC
JAEZNNZEAJ
WJAKCGSGCF
QKUDGATDQL
OKGPFPYRKQ
TDCXBMQTIO
UNADRPNETZ
ZATWDEKDQF
10 10
WPMACSIBIK
STWASDCOBQ
AMOUENCSOG
XTIIGBLRCZ
WXVSWXYYVU
CJVAHRZZEM
NDIEBIIMTX
UOOGPQCBIW
OWWATKUEUY
FTMERSSANL
20 13
ECFQBKSYBBOSZQSFBXKI
VBOAIDLYEXYMNGLLIOPP
AIZMTVJBZAWSJEIGAKWB
CABLQKMRFNBINNZSOGNT
NQLMHYUMBOCSZWIOBINM
QJZQPSOMNQELBPLVXNRN
RHMDWPBHDAMWROUFTPYH
FNERUGIFZNLJSSATGFHF
TUIAXPMHFKDLQLNYQBPW
OPIRADJURRDLTDKZGOGA
JHYXHBQTLMMHOOOHMMLT
XXCNJGTXXKUCVOUYNXZR
RMWTQQFHZUIGCJBASNOX
CVODFKWMJSGMFTCSLLWO
EJISQCXLNQHEIXXZSGKG
KGVFJLNNBTVXJLFXPOZA
YUNDJDSSOPRVSLLHGKGZ
OZVTWRYWRFIAIPEYRFFG
ERAPUWPSHHKSWCTBAPXR
FIKQJTQDYLGMMWMEGRUZ

[출력]
#1 JAEZNNZEAJ
#2 MWOIVVIOWM
#3 TLMMHOOOHMMLT
============================================
'''

test_case = int(input())

def searching_algo(N,M,data_list,t):
  for i in range(N):
    for j in range(N-M+1):
      data_word = data_list[i][j:j+M]
      reversed_list = reversed(list(data_word))
      reversed_word = ''.join(str(e) for e in list(reversed_list))
      if data_word == reversed_word:
        print("#{0} {1}".format(t+1,data_word))


for t in range(test_case):
  N, M = map(int, input().split())
  horizental = [input() for _ in range(N)]
  new_list = [[0 for _ in range(N)] for _ in range(N)]
  vertical = []
  for i in range(N):
    for j in range(N):
      new_list[i][j] = horizental[j][i]
    vertical.append(''.join(str(e) for e in new_list[i]))


  searching_algo(N,M,horizental,t)
  searching_algo(N,M,vertical,t)