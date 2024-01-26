import os
import os.path
import shutil
import os,os.path,re,time
from datetime import datetime,timedelta
def moveExport():
    d=(datetime.today()+timedelta(days=-1)).strftime('%Y-%m-%d %H:%M:%S')
    filelist=[]
    path = '//srv046/avm-rkf_export'
    t=time.strptime(d, "%Y-%m-%d %H:%M:%S")
    t= time.mktime(t)
    for root, dirs, files in os.walk(path):
        for file in files:
            path= os.path.join(root, file)
            if (not re.match(r".*(\.svn|\.project|html\.\d+|Thumbs\.db|.py|.bat|IPR curves .xlsx|20220425 Well tests comparison.xlsx|V-102 WT history.xlsx).*", path)):
                filelist.append(path)
    for i in filelist:
        if os.path.getmtime(i)>t:
            shutil.copy(i, '//192.168.147.12/Public/03.SUBSURFACE/RKF_DATA_MANAGEMENT/AVM-RKF_EXPORT')     