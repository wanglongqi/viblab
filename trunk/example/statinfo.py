# -*- coding:utf-8 -*-
'''该脚本对测试数据进行一些统计信息的分析。

注意：所有数据均以csv格式导出，这可能在某些情况下很慢。

Created on 2011-12-28

@author: WLQ
'''
import glob 
import os

#Output file name define
#在chdir之前定义，可以保证程序输出在当前目录，否则会输出到chdir后的目录。代码按需放置。

info=open('Info.csv','a')
movingpeak=open('MovingPeak.csv','a')
movingrms=open('RMS.csv','a')
spec=open('Spec.csv','a')

movingpeakw=open('MovingPeakWeighted.csv','a')
movingrmsw=open('RMSWeighted.csv','a')
movingcrest=open('MovingCrest.csv','a')
specw=open('SpecWeight.csv','a')

os.chdir(ur'SOMEWHERE')
mnum='3'
files=glob.glob('*.tsp')
import viblab as vl
files=vl.DASPName(files)
lastfs=0

step=2560
points=2560

for fname in files.getmnum(mnum):
    data=vl.dsp2ary(fname+'.tsp')
    newfs=data[1]['Fs']
    if lastfs!=newfs:
        lastfs=newfs
        zf=vl.Weight(newfs,method='Wk')
#        Output head info
        info.write('FileName,Peak,RMS,Peak(W),RMS(W),Crest,VDV\n')
    filtdata=zf.filter(data[0])
#    Output what we want
    info.write('%s,%g,%g,%g,%g,%g,%g\n'%
        (fname,vl.peak(data[0]),vl.rms(data[0]),vl.peak(filtdata),vl.rms(filtdata),vl.crest(filtdata),vl.vdv(filtdata,newfs)))
    movingpeak.write(fname+','+str(vl.fastmoving(vl.peak,data[0],step,points).tolist())[1:-1]+'\n')
    movingrms.write(fname+','+str(vl.fastmoving(vl.rms,data[0],step,points).tolist())[1:-1]+'\n')
    movingpeakw.write(fname+','+str(vl.fastmoving(vl.peak,filtdata,step,points).tolist())[1:-1]+'\n')
    movingrmsw.write(fname+','+str(vl.fastmoving(vl.rms,filtdata,step,points).tolist())[1:-1]+'\n')
    movingcrest.write(fname+','+str(vl.fastmoving(vl.crest,filtdata,step,points).tolist())[1:-1]+'\n')
    spec.write(fname+','+str(vl.spec.periodogram.speriodogram(data[0],NFFT=points,sampling=newfs).tolist())[1:-1]+'\n')    
    specw.write(fname+','+str(vl.spec.periodogram.speriodogram(filtdata,NFFT=points,sampling=newfs).tolist())[1:-1]+'\n')

info.close()    
movingpeak.close()
movingrms.close()
spec.close()

movingpeakw.close()
movingrmsw.close()
movingcrest.close()
specw.close()
    
    
    



