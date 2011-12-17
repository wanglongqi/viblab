# -*- coding:utf-8 -*-
'''
Created on 2011-12-5

@author: WLQ
'''
import numpy as np
import os
import sys

def ParseTsp(fid):
    'This function parses the tsp file to get infomation about the testing data.'
    info={}
    line=fid.readline().split(',')
    info['Fs']=eval(line[0])
    info['Amp']=eval(line[5])
    info['Sens']=eval(line[7])
    info['Unit']=eval(line[-1])
    line=fid.readline()
    info[u'测点位置']=line
    line=fid.readline()
    line=fid.readline()
    info[u'实验对象']=line
    return info 

def dsp2ary(file):
    '''This function read the testing data into memory, the output value is a tuple include
a ndarry(data) and a dict(information about the testing data).'''
    try:
        fname,ext=os.path.splitext(file)
        if ext.lower()!='.tsp':
            pass
        else:                
            info=ParseTsp(open(file))
            tspfile=open(file).read()
            data=np.fromfile(fname+'.sts',dtype=np.float32)
            data=data/info['Amp']/info['Sens']
            info['Lens']=len(data)
            info['FileName']=fname
            info['OriginFile']=tspfile
            return (data,info)
    except Exception,msg:
        print >>sys.stderr, 'Failed in converting '+file+'. \n  >>  Error information:',
        print >>sys.stderr, msg
        pass

def dsp2mat(files):
    '''This function convert the testing data into Matlab .mat file.
The mat file contains the testing data and infomation about the testing data, too.'''
    import glob
    import scipy.io as sio
    import scipy.io.matlab.streams  #This line is used to compile this file
    files=glob.glob(files)
    for file in files:
        try:
            d,i=dsp2ary(file)
            Data={'Data':d,'Lens':i['Lens'],'Fs':i['Fs'],'Unit':i['Unit']}
            sio.savemat(i['FileName']+'.mat',Data,appendmat=True, format='5', 
                long_field_names=False, do_compression=True, oned_as='column')
        except:
            pass

if __name__=='__main__':
    if len(sys.argv)>1:
        dsp2mat(sys.argv[1])
    else:
        print os.path.relpath(sys.argv[0])+' filepattern'
        print '         Convert DASP testing data to Matlab .mat file'
