# -*- coding:utf-8 -*-
'''
Created on 2011-12-23

@author: WLQ
由于Numpy的默认窗函数没有做周期处理，对谱分析会有一些影响，因此使用Scipy中的窗函数替代。
以下是Scipy支持的窗函数类型：
boxcar, triang, blackman, hamming, hanning, bartlett, parzen, bohman, blackmanharris, 
nuttall, barthann, kaiser (needs beta), gaussian (needs std), 
general_gaussian (needs power, width), slepian (needs width), chebwin (needs attenuation)

在此仅导入Numpy中提供的窗函数：
bartlett  
blackman  
hamming  
hanning  
kaiser 
'''
import scipy.signal as ss
import numpy as np
def rect(Nx):
    'Return the Rectangle window.'
    return np.ones(len(Nx))

def bartlett(Nx):
    'Return the Bartlett window.'
    return ss.get_window('bartlett',Nx,fftbins=True) 
    
def blackman(Nx):
    'Return the Blackman window.'
    return ss.get_window('blackman',Nx,fftbins=True) 
    
def hamming(Nx):
    'Return the Hamming window.'
    return ss.get_window('hamming',Nx,fftbins=True) 
        
def hanning(Nx):
    'Return the Hanning window.'
    return ss.get_window('hanning',Nx,fftbins=True) 

hann=hanning #Wrap for matlab

def kaiser(Nx,beta):
    'Return the Kaiser window.'
    return ss.get_window(('kaiser',beta),Nx,fftbins=True)

def get_window(*args,**kargs):
    'Call scipy.signal.get_window directly.'
    return ss.get_window(*args,**kargs)
