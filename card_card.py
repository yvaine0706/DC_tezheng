# -*-coding:utf-8 -*-
import time
import numpy as np
import pdb
import math

st = time.time()

path1='e:/DC/test/card_test.txt'
path2='e:/DC/test/tz1/c_card_test.csv'
L=[]
k=0
with open(path1,'r') as f1:
    lines = f1.readlines()    
    for line in lines:
#         if k <= 15000000:     
#             k=k+1
#         elif k>13000000 and k<=14000000:
#             k=k+1
        lswt = []
        lst=line.split(',')
        lst = map(lambda x:x.strip(), lst)
        if lst[1]=='"卡充值"':
            lswt.append(lst[0])
            lswt.append(lst[5])
            L.append(','.join(map(lambda x:str(x), lswt)))
with open(path2, 'wb') as fw:
    fw.writelines('\n'.join(L))        

ed = time.time()

print ed -st
