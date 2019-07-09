#!/usr/bin/env python
#!coding:utf-8

import os
import struct

def get_adaptation_field_control(b3):
    adaptation_field_control =  (b3 >>4) & 0b11
    return adaptation_field_control

def get_pid(b1,b2):
    pid = (((b1 & 0b11111) << 8) | b2)
    return pid


def get_pcr(ff):
    pcr_time= 0
    pcr_bash = 0
    pcr_time = 0
    while True:
        _buf = ff.read(188)
        buf = struct.unpack("B" * len(_buf), _buf)
        if not buf:
            print "pcr 时间为 %f" %(pcr_time/90000)
            return
        #print 123
        adaption_field_control = get_adaptation_field_control(buf[3])
        pid = get_pid(buf[1],buf[2])
        if adaption_field_control ==0b10 | adaption_field_control==0b11:
            PCR_flag = (buf[5]>>4) &0b1
            if PCR_flag ==1:
                #print pid
                if not pcr_bash:
                    pcr_bash = (buf[6] << 25) | buf[7] << 17 | buf[8] << 9 | buf[9] <<1 | buf[10]>>7
                    continue
                pcr_now = (buf[6] << 25) | buf[7] << 17 | buf[8] << 9 | buf[9] <<1 | buf[10]>>7
                #print pcr_time
                pcr_time = pcr_time + pcr_now -pcr_bash
                pcr_bash = pcr_now
                #print "pcr = %d" %pcr
    return
if __name__ == '__main__':
    import os
    import sys
    fi = sys.argv
    if not os.path.exists(fi[1]):
        print "文件不存在"
        sys.exit(0)
    with open(fi[1],"r") as f:
        get_pcr(f)
