#!/usr/bin/py
# filename=RPDownloader.py

from modules.Utils import e2csv
from modules.Fi import tcode
import pandas as Pd
import requests as ro

def downloadBSRP(stocklist):
    num = 0
    for c in stocklist:
        bs_url='http://soft-f9.eastmoney.com/soft/gp15.php?code={co}01&exp=1'.format(co=tcode(c))
        ct = ro.get(bs_url).text
        to_file='bs{co}.csv'.format(co=tcode(c))
        open(to_file,'w').write(e2csv(ct))
        num = num + 1
        
    return num