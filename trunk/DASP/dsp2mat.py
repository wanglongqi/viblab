# -*- coding:utf-8 -*-
'''
该文件将DASP导出的包括长度，采样频率等的ASCII码文件转换成.mat文件，方便后续使用。
Created on 2011-9-1

@author: WLQ
'''
from scipy.io import savemat
from numpy import loadtxt
from glob import glob
import sys
from time import clock
if len(sys.argv)>1:
    files=[]
    for i in xrange(1,len(sys.argv)):
        files.extend(glob(sys.argv[i]))
else:
    print '''#==================================================================#
#            DASP DAT to Matlab Files Converter                    #
#               Author: WLQ   Date: 2011-9-1                       #
#==================================================================#
    '''
    print 'FileName or Patterns:',
    try:
        files=glob(raw_input())
    except:
        sys.exit()

for file in files:
    try:
        print 'Loading '+file+'...  CP:',clock()
        head,fnameext=os.path.split(file)
        fname,ext=os.path.splitext(fnameext)
        file_name=os.path.join(head,fname)
        f=open(file)
        data={}
        line=f.readline().split()
        data['Fs']=float(line[-1])
        line=f.readline().split()
        data['Len']=float(line[-1])
        line=f.readline().split()
        data['Unit']=line[-1]
        f.close()
        data['Data']=loadtxt(file,skiprows=3)   
        print 'Saveing date to '+file_name+'.mat...  CP:',clock()     
        savemat(file_name, data, appendmat=True, format='5', 
            long_field_names=False, do_compression=True, oned_as='column') 
    except Exception,msg:
        print >>sys.stderr, 'Failed in converting '+file+'. \n  >>  Error information:',
        print >>sys.stderr, msg
        pass
