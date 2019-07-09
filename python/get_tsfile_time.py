#!/usr/bin/env python
#coding:utf-8
import os
import struct

def _get_adaptation_field_control(b3):
    adaptation_field_control =  (b3 >>4) & 0b11
    return adaptation_field_control

def _get_pid(b1,b2):
    pid = (((b1 & 0b11111) << 8) | b2) 
    return pid 


def get_time(ff):
    pcr_bash = 0 
    PCR_flag = 0
    buff = struct.unpack("B" * len(ff), ff)
    for i in range(len(buff)/188):
	buf = buff[i*188:(i+1)*188]
        adaption_field_control = _get_adaptation_field_control(buf[3])
       	pid = _get_pid(buf[1],buf[2])
        if adaption_field_control ==0b10 | adaption_field_control==0b11:
       		PCR_flag = (buf[5]>>4) &0b1
        	if PCR_flag ==1:
        		if not pcr_bash:
                    		pcr_bash = (buf[6] << 25) | buf[7] << 17 | buf[8] << 9 | buf[9] <<1 | buf[10]>>7
				continue
    a=(pcr_bash)/90000.0
    return a
if __name__ == '__main__':
    import os
    import sys 
    fi = sys.argv
    if not os.path.exists(fi[1]):
        sys.exit(0)
    with open(fi[1],"r") as f:
        get_time(f)

