# -*- coding:utf-8 -*-
'''
Created on 2011-12-19

@author: WLQ
'''


from guidata.dataset.datatypes import DataSet, BeginGroup, EndGroup
from guidata.dataset.dataitems import (FloatItem, IntItem, StringItem, TextItem, FileOpenItem)
from ary2dsp import ary2dsp
import numpy as np
from guidata.configtools import get_icon
from PyQt4 import QtGui as QG

class Info(DataSet):
    """Input Info About Data
    Please input infomation about the given data:
    Data File: Data File to be Converted
    SkipRows: Skip how many rows before reading data
    Fs: Fs of the data
    Lens: Length of the data
    Unit: Unit of the data
    ExpName: Experiment Name
    ExpCount: The counter of the experiment
    ChanelNum: The Start of Chanel Number
    """
    Fname = FileOpenItem("Data File: ")
    SkipRows = IntItem('SkipRows:',min=0,default=0)
    Fs = FloatItem('Fs: ',min=0,default=250)
    Lens= IntItem('Lens:',min=0,default=0)
    Unit= StringItem('Unit:',default='m/ss')
    ExpName=StringItem('ExpName',default='Test')
    ExpCount=IntItem('ExpCount:',min=1,default=1)
    ChanelNum=IntItem('ChanelNum:',min=1,default=1) 

def ffunc(dialog):
    'Return output filename'
    count=dialog.ChanelNum
    while True:
        yield dialog.ExpName+str(dialog.ExpCount)+'#'+str(count)
        count+=1           
    
if __name__ == "__main__":
    # Create QApplication
    import guidata
    _app = guidata.qapplication()
    dialog=Info(icon=QG.QIcon('../viblab.png'))
    #Load default information if exist
    try:
        import default
        dialog.Fs=default.Fs
        dialog.Lens=default.Lens
        dialog.Unit=default.Unit
        dialog.SkipRows=default.SkipRows
        dialog.ExpName=default.ExpName
        dialog.ExpCount=default.ExpCount
        dialog.ChanelNum=default.ChanelNum        
    except:
        pass
    
    while(dialog.edit()):
        try:
            data=np.loadtxt(dialog.Fname,skiprows=dialog.SkipRows)
        except Exception,msg:
            print 'Load data file Error!\n',msg
        if dialog.Lens==0:
            dialog.Lens=data.shape[0]
        dialog.view()
        info={'Fs':dialog.Fs,
            'Lens':dialog.Lens,
            'Unit':dialog.Unit,                        
        }
        fgen=ffunc(dialog)
        ary2dsp(data,info,fgen)
        

