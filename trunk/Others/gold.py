#! coding:utf8
import sys
import StringIO
import urllib
import re
from lxml import etree
import time
newinfo=''
parser = etree.HTMLParser(encoding='utf8')
while 1:
    try:
        oldinfo=newinfo
        page=urllib.urlopen("http://www.icbc.com.cn//ICBCDynamicSite/Charts/GoldTendencyPicture.aspx")
        data = page.read()
        page.close()
        
        doc = etree.parse(StringIO.StringIO(data),parser)
        tr=doc.xpath('//*[@id="GridView1"]/tr[6]')
        td=tr[0].getchildren()
        newinfo=td[0].text.strip()+' '+td[3].text.strip()+' '+td[4].text.strip()+' '+td[5].text.strip() 
        if oldinfo!=newinfo:
            print newinfo,time.ctime()
        time.sleep(15)
    except KeyboardInterrupt:
        break
    except:
        time.sleep(1)
        pass
        