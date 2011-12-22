# -*- coding:utf-8 -*-
'''
Created on 2011-12-22

@author: WLQ
返回正确的身份证末位校验码
'''
import sys
def checksum(chars):
    str2num={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'x':10,'X':10}
    if len(chars)==17:
        chars=chars+'0'
    else:
        chars=chars[:17]+'0'
    sum=0
    for index,char in enumerate(chars):
        ind=18-index
        weight=2**(ind-1)%11
        sum=(sum+str2num[char]*weight)%11
    sum=(1-sum)%11
    if sum==10:
        return chars[:17]+'X'
    else:
        return chars[:17]+str(sum)

if __name__=='__main__':
    if len(sys.argv)>1:
        for arg in sys.argv[1:]:
            print checksum(arg)
    else:
        print sys.argv[0]+' Return the checksum as it should be.'