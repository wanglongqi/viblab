# -*- coding:utf-8 -*-
'''
Created on 2011-12-17

该文件没有完整注释，也没有通过详细调试，可能会有巨大的BUG.
@author: WLQ
'''
import numpy as np
import os
def WriteTsp(fid,info):
    if info.has_key('OriginFile'):
        fid.write(info['OriginFile'])
    else:
        if not info.has_key('Fs'):
            raise Exception,'Fs not found in the given information'
        if not info.has_key('Lens'):
            raise Exception,'Lens not found in the given information'
        if not info.has_key('Amp'):
            info['Amp']=1.0 #morfvfyiwzyi
        if not info.has_key('Sens'):
            info['Sens']=1.0 #morfl;m;duwzyi 
        if not info.has_key('Unit'):
            info['Unit']='mV' #morfdjwzwzhkfu
        if not info.has_key(u'测点位置'):
            info[u'测点位置']=''
        if not info.has_key(u'实验对象'):        
            info[u'实验对象']=''
        if not info.has_key(u'FileName'): 
            info['FileName']=''
        fid.write('''%f,111,%d,%d,1,%f,1,%f,"%s"
%s

%s
[DASP-TSP-MORE-PARA]
FileVersion=1.0
[Source]
Source=Translate by VibLab
'''%(info['Fs'],info['Lens']/512,info['Lens']%512,info['Amp'],info['Sens'],info['Unit'],info[u'测点位置'],info[u'实验对象']))

def ary2sts(ary,fgen):
    if len(ary.shape)==1:
#        'Vector'
        ary.astype(np.float32).flatten().tofile(fgen.next())
    else:
        for col in range(ary.shape[1]):
            ary[:,col].astype(np.float32).tofile(fgen.next())

def sample_filename_generator(head):
    count=1
    while 1:
        yield head+'#'+str(count)
        count+=1

def vec2dsp(vec,info,ofile=None):
    if ofile==None:
        if not info.has_key(u'FileName'):
            ofile='test1#1'
        else:
            ofile=info['FileName']
    else:
        ofile,ext=os.path.splitext(ofile)
    tsp=open(ofile+'.tsp','w')
    WriteTsp(tsp, info)
    tsp.close()
    vec.astype(np.float32).flatten().tofile(ofile+'.sts')

def ary2dsp(ary,info,ffunc):
    for col in range(ary.shape[1]):
        ofile=ffunc.next()
        tsp=open(ofile+'.tsp','w')
        WriteTsp(tsp, info)
        tsp.close()
        ary[:,col].astype(np.float32).tofile(ofile+'.sts')   
