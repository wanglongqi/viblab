# -*- coding:utf-8 -*-
'''
Created on 2011-12-21

@author: WLQ

现在仅提供Wk的计权方式。

注：该程序的计权使用的是标准附录A的滤波器，可能和直接使用计权曲线计算得到的计权结果有所不同。
'''
import numpy as np
import scipy.signal as ss

class Weight(object):
    def __init__(self,Fs,method='Wk'):
        'method is always "Wk"'
        Hhb=[1,0,0]
        Hha=[1,3.55430635052669,6.31654681669719] 
        Hlb=[394784.176043574]
        Hla=[1,888.576587631673,394784.176043574]   
        Htb=[0.0127323954473516,1]
        Hta=[0.000162113893827740,0.0202101515037327,1]    
        Hsb=[1,16.3639001956216,221.746323841915]
        Hsa=[1,23.1304074495073,443.046541564901]
        self._Hh=ss.bilinear(Hhb,Hha,fs=Fs)
        self._Hl=ss.bilinear(Hlb,Hla,fs=Fs)
        self._Ht=ss.bilinear(Htb,Hta,fs=Fs)
        self._Hs=ss.bilinear(Hsb,Hsa,fs=Fs)
    
    def filter(self,data):
        'filter given data'
        return ss.lfilter(self._Hs[0],self._Hs[1],
            ss.lfilter(self._Ht[0],self._Ht[1],
                ss.lfilter(self._Hl[0],self._Hl[1],
                    ss.lfilter(self._Hh[0],self._Hh[1],data))))

    
