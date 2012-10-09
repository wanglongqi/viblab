# -*- coding:utf-8 -*-
'''
Created on 2012-5-24

@author: WLQ
贵金属价格美元至人民币兑换程序，使用了Sina提供的汇率
'''
import urllib2
import sys
import os

exchange=float(urllib2.urlopen("http://hq.sinajs.cn/list=USDCNY").read().split(',')[7])
if len(sys.argv)>1:
    for price in sys.argv[1:]:
        if price.find('$')==-1:
            print price,'CNY/g = %.2f USD/oz'%(float(price)*31.1035/exchange)
        else:
            price=price.replace('$','')
            print price,'USD/oz = %.2f CNY/g'%(float(price)/31.1035*exchange)
else:
    print 'Usage:',os.path.relpath(sys.argv[0]),'''PRICE
    PRICE: price in CNY/gram or USD/oz(with $), eg 20.1 or 1530.35$'''
        
