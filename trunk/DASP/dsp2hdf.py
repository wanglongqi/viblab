# -*- coding:utf-8 -*-
'''
Created on 2011-12-17

@author: WLQ
'''
import h5py
import numpy as np
import os
import sys

def ParseTsp(fid):
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

def dsp2hdf(out,ins):
    ofile=h5py.File(out,'a')    
    for file in ins:
        try:
            fname,ext=os.path.splitext(file)
            if ext.lower()!='.tsp':
                pass
            else:                
                info=ParseTsp(open(file))
                tspfile=open(file).read()
                data=np.fromfile(fname+'.sts',dtype=np.float32)
                data=data/info['Amp']/info['Sens']
                ds=ofile.create_dataset(unicode(fname.decode('gbk')), data=data,compression='gzip')
                for key in info:
                    ds.attrs[key]=info[key]
                ds.attrs['Lens']=len(data)
                ds.attrs['FileName']=fname
                ds.attrs['OriginFile']=tspfile
                ofile.flush()
        except Exception,msg:
            print >>sys.stderr, 'Failed in converting '+file+'. \n  >>  Error information:',
            print >>sys.stderr, msg
            pass
    ofile.close()

        
             
 



