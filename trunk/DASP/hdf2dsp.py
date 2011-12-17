# -*- coding:utf-8 -*-
'''
Created on 2011-12-17

@author: WLQ
'''
from ary2dsp import vec2dsp
import h5py
import sys
def hdf2dsp(fname):
    hdf=h5py.File(fname,'r')
    for key in hdf.keys():
        info=dict(hdf[key].attrs.items())
        data=hdf[key].value
        vec2dsp(data, info)
    hdf.close()

if __name__=='__main__':
    if len(sys.argv)>1:
        hdf2dsp(sys.argv[1])
    else:
        print os.path.relpath(sys.argv[0])+' filepattern'
        print '         Convert DASP testing data to HDF5 file.'
