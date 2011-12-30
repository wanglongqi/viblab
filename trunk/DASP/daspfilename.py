# -*- coding:utf-8 -*-
'''该模块分析DASP文件列表的文件名，并进行分组。
DASP的文件名方式为：
实验名称 + 测试号 + # + 测点号 +后缀

Created on 2011-12-28

@author: WLQ
'''
import re
class DASPName(object):
    'Group file list by the FileName'
    fre=re.compile('(.*[^0-9])([0-9]+)#([0-9]+.*)\.tsp',re.IGNORECASE)
    def __init__(self,files):        
        gf={}
        for fname in files:
            tmp=DASPName.fre.match(fname)
            if tmp==None:
                pass
            else:
                expname,tnum,mnum=tmp.groups()
                if expname in gf.keys():
                    if tnum in gf[expname].keys():
                        gf[expname][tnum].append(mnum)
                    else:
                        gf[expname][tnum]=[mnum]                    
                else:
                    gf[expname]={tnum:[mnum]}
        self.files=gf
    
    def getexp(self,name):
        flist=[]
        if name in self.files.keys():            
            brunch=self.files[name]
            for tnum in brunch.keys():
                for mnum in brunch[tnum]:
                    flist.append(name+tnum+'#'+mnum)
        return flist
            

    def gettnum(self,name):
        flist=[]
        for expname in self.files.keys():            
            brunch=self.files[expname]
            if name in brunch.keys():
                for mnum in brunch[name]:
                    flist.append(expname+name+'#'+mnum)
        return flist                    

    def getmnum(self,name):
        flist=[]
        for expname in self.files.keys():            
            brunch=self.files[expname]
            for tnum in brunch.keys():
                if name in brunch[tnum]:
                    flist.append(expname+tnum+'#'+name)
        return flist                 
    