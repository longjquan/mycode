#!/usr/bin/env python
#!coding:utf-8

import socket
import struct
import time
import sys
from gettime import *
#from tstime import *

host = ("0.0.0.0",11150)
#pmt_pid = 0 
heard ="#EXTM3U \n#EXT-X-VERSION:3\n#EXT-X-ALLOW-CACHE:YES\n#EXT-X-MEDIA-SEQUENCE:1\n#EXT-X-TARGETDURATION:15\n"
mid = "#EXTINF:%f,\n"
end ="#EXT-X-ENDLIST"

def now_time():
    return time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())

def server(host):
    s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(host)
    print "连接用户"
    return s

def do(conn,ff):
    pcr_bash = 0
    ts_time=float(0)
    filename = now_time()
    #print "begin ok"
    name = "./live/"+ filename + ".ts"
    with open(name, "wb") as f:
        while True:    
	    pcr_now = 0        
	    buff, addr = conn.recvfrom(1316)
            _buf = struct.unpack("B"*len(buff),buff)
	    f.write(buff)
	    f.flush()
	    if not pcr_bash:
		pcr_bash = get_time(buff)
	    nowtime = get_time(buff)
	    ts_time=nowtime - pcr_bash
	    if ts_time>20:
		continue	   
	    if (ts_time) >=10:
                ff.write(mid%ts_time)
                ff.write(filename +".ts" +"\n")
                ff.flush()
                return
	    
if __name__ == '__main__':
    conn = server(host)
    with open("live/live.m3u8","a") as ff:
	    ff.write(heard)
	    while True:
        	do(conn,ff)

