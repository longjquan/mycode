#!/usr/bin/env python
#!coding:utf-8

import os
import sys
import time
import datetime
import getduration  ##计算ts文件时长脚本，已经上传。
from sys import argv

stime=argv[2]  #设定m3u8文件截取的开始时间
etime=argv[3]  #设定m3u8文件结束时间
#stime="2019-02-17_20-50-00"
#etime="2019-02-17_20-53-00"
starttime=datetime.datetime.strptime(stime, "%Y-%m-%d_%H:%M:%S")
endtime=datetime.datetime.strptime(etime,"%Y-%m-%d_%H:%M:%S")

##获取ts文件时长duration = getduration.GetDuration(os.path.join(self.store_path, ts))
heard="#EXTM3U \n#EXT-X-VERSION:3\n#EXT-X-ALLOW-CACHE:YES\n#EXT-X-MEDIA-SEQUENCE:1\n#EXT-X-TARGETDURATION:15\n"
end="#EXT-X-ENDLIST"
path=os.path.join('/data',str(argv[1]))
#path="/home/quan/桌面/m3u8/ts_file"
#with open('/home/quan/桌面/m3u8/ts_file/new.m3u8','a') as f:

def ts_list(stime,etime):
    res=[]
    file_names=os.walk(path)
    for root,dirs,files in file_names:
        for file_name in files:
            if not file_name.endswith(".ts"):
                continue
            #s=file_name.find('-')
            e=file_name.find('.')
            ts_time=datetime.datetime.strptime(file_name[:e], "%Y-%m-%d_%H:%M:%S")
            if ts_time>starttime and ts_time<endtime:
                res.append(file_name)
    res.sort()
    return res

def write_m3u8():
    aa=ts_list(starttime,endtime)
    with open(path+'/'+"a.m3u8",'a') as f:
        f.write(heard)
        for i in aa:
            tstime=getduration.GetDuration(path+'/'+i)
            f.write("#EXTINF:"+str(tstime)+",\n")
            f.write(i+"\n")
#    f.close()

if __name__=='__main__':
    write_m3u8()
    with open(path + '/' + "a.m3u8", 'a') as f:
        f.write(end)
        f.close()
    print "ok"

                                                                                                                                                                                                
