# -*- coding:utf-8 -*-
'''
Created on 2011-12-19

@author: WLQ
'''
from ary2dsp import ary2dsp
import sys
import numpy as np
import optparse
def verbose():
    if options.verbosity>0:
        print 'Please Check Data File Info:'
        print 'Fs: ',Fs,
        print '\tLens:',Lens,
        print '\tUnit: ',Unit
    
    if options.verbosity>1:
        print '\nDo you want to execute the convertion?(y/N)'
        if raw_input()=='N':    
            print 'User Abort.'
            return False
    return True
def ffunc():
    'Return output filename'
    count=ChanelNum
    while True:
        yield ExpName+str(ExpCount)+'#'+str(count)
        count+=1     

parser = optparse.OptionParser(version="%prog 1.0alpha")

parser.add_option('-i', '--info',
        dest='info',
        help='infomation, info file about the data file.',
        )
parser.add_option('-d','--demo',
        dest='demo',
        help='output a demo file for info file.',
        action="store_true", 
        default=False
        )        
parser.add_option("-v",
        action="count", 
        help='verbosity, dupulicate v to get more details.',
        dest="verbosity"
        )
parser.add_option('-s','--skip-rows',
        dest='skiprows',
        help='skip n rows of data file.',
        type='int'
        )
options, others = parser.parse_args()

if others==[]:    
    others.append(sys.stdin)
  
if options.demo:
    print '''Fs=1024
Lens=0
Unit='m/ss'
SkipRows=3
ExpName='Test'
ExpCount=1
ChanelNum=1
'''
    sys.exit()

if options.info==None:
    print 'Error: no info file provided. Use -h option to view help informations.'
    sys.exit(1)
    
execfile(options.info)

if options.skiprows!=None:
    SkipRows=options.skiprows
    
info={'Fs':Fs,
    'Lens':Lens,
    'Unit':Unit,                        
}

fgen=ffunc()

for file in others:
    data=np.loadtxt(file,skiprows=SkipRows)
#    data=np.loadtxt(file,dtype=np.float32,skiprows=SkipRows) 这一行没有使得内存占用更小，也没事的运行更快，反而更慢，因此不采用。
    if options.verbosity>0:
        print str(file)+' is loaded to memory.'
    if Lens==0:
        Lens=data.shape[0]
        if verbose():
            ary2dsp(data,info,fgen)
        Lens=0
    else:
        if verbose():
            ary2dsp(data,info,fgen)
    if options.verbosity>0:
        print str(file)+' is saved to the disk.'
    
