#!/usr/bin/env python
#!coding:utf-8

import struct
files = "/home/quan/桌面/ts/live-2019-05-24_21-48-03.ts"

def Do(files,ff):
    f = open(files,"r")
    n = 0
    while True:
        _buf =f.read(188)
        if not _buf:
            print "已经读取完毕！！"
            print "pcr时间为：%d" %pcr_time
            return
        buf = struct.unpack("B" * len(_buf), _buf)
        if buf[0] != 0x47:
            continue
        if get_pid(buf[1],buf[2]) == 0:
            continue
        get_pmt_stream(buf)

    return

def get_pid(b1,b2):
    pid = (((b1 & 0b11111) << 8) | b2)
    return pid

def get_payload_unit_start_indicator(b1):
    payload_unit_start_indicator = (b1 >> 6) & 0b01
    return payload_unit_start_indicator

def get_transport_error_indicator(b1):
    transport_error_indicator = b1>>7
    return transport_error_indicator

def get_transport_priority(b1):
    transport_priority = (b1>>5)&0x1
    return transport_priority

def get_transport_scrambling_control(b3):   #加密标志（00：未加密；其他表示已加密）
    transport_scrambling_control = b3>>6
    return transport_scrambling_control

def get_adaptation_field_control(b3):
    adaptation_field_control =  (b3 >>4) & 0b11
    return adaptation_field_control

def get_continuity_counter(b3):
    continuity_counter = b3 & 0b1111
    return continuity_counter

def get_pmt_pid(buf):
    payload_unit_start_indicator = get_payload_unit_start_indicator(buf[1])
    #print "payload_unit_start_indicator = %d" % payload_unit_start_indicator
    if payload_unit_start_indicator == 1:
        program_number = (buf[13] <<8) | buf[14]
        program_map_PID = ((buf[15]<<8) | buf[16]) &0b1111111111111
        return program_number,program_map_PID
    else:
        program_number = (buf[12] << 8) | buf[13]
        program_map_PID = ((buf[14] << 8) | buf[15]) & 0b1111111111111
        return program_number, program_map_PID

def get_pmt_stream(buf):
    payload_unit_start_indicator = get_payload_unit_start_indicator(buf[1])
    streams_id = {}
    if payload_unit_start_indicator ==1:
        section_length = ((buf[6] & 0b1111)<<8) | buf[7]
        #n = (section_length - 13) / 5  # section_length为后续有用数据的字节数，减去固定项目就是音视频流的信息条数了。
        pcr_pid =(buf[13]) & 0b1111111111111 | buf[14]
        n =17
        while 1:
            stream_type = buf[n]
            if get_pid(buf[1],buf[2]) !=get_pmt_pid(buf):
                continue
            elementary_PID = ((buf[n+1] & 0b11111) << 8) | buf[n+2]
            ES_info_length = (buf[n+3] & 0b1111) << 8 | buf[n+4]
            streams_id[elementary_PID] = stream_type
            n = ES_info_length + n+ 5
         #   print "elementrry_id = %d" %elementary_PID
         #   print "n= %d,es_info_len= %d" %(n,ES_info_length)
            if (n + 4) > section_length:
                break
    else:
        section_length = ((buf[5] & 0b1111) << 8) | buf[6]
        # n = (section_length - 13) / 5  # section_length为后续有用数据的字节数，减去固定项目就是音视频流的信息条数了。
        pcr_pid = (buf[12]) & 0b1111111111111 | buf[13]
        n = 16
        while 1:
           # print len(buf)
            #for i in buf:
             #   print i
            stream_type = buf[n]
            elementary_PID = ((buf[n + 1] & 0b11111) << 8) | buf[n + 2]
            ES_info_length = (buf[n + 3] & 0b1111) << 8 | buf[n + 4]
            streams_id[elementary_PID] = stream_type
            n += ES_info_length
            if (n + 4) > section_length:
                break
    print  streams_id
    return

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
                #return pcr


if __name__ == '__main__':
    with open("/home/quan/桌面/ts/live-2019-05-24_21-48-03.ts","r") as ff:
        Do(files,ff)
