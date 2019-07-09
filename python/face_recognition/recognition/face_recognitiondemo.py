#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 识别人脸鉴定是哪个人

# 导入face_recogntion模块，可用命令安装 pip install face_recognition
import face_recognition

#将jpg文件加载到numpy数组中
liu_image = face_recognition.load_image_file("liu.jpeg")
liming_image = face_recognition.load_image_file("liming.jpeg")
#要识别的图片
unknown_image = face_recognition.load_image_file("liming.jpeg")

#获取每个图像文件中每个面部的面部编码
#由于每个图像中可能有多个面，所以返回一个编码列表。
#但是由于我知道每个图像只有一个脸，我只关心每个图像中的第一个编码，所以我取索引0。
liming_face_encoding = face_recognition.face_encodings(liming_image)[0]
liu_face_encoding = face_recognition.face_encodings(liu_image)[0]
#print("chen_face_encoding:{}".format(liu_face_encoding))
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
#print("unknown_face_encoding :{}".format(unknown_face_encoding))

known_faces = [
    liu_face_encoding,liming_face_encoding
]
#结果是True/false的数组，未知面孔known_faces阵列中的任何人相匹配的结果
results = face_recognition.compare_faces([liu_face_encoding], unknown_face_encoding)

if results:
	print ("这个人是刘德华")


#name = known_faces[first_match_index]

	print("result :{}".format(results))
#print ("这个人是刘德华")

#print("这个未知面孔是 陈都灵 吗? {}".format(results[0]))
#print("这个未知面孔是 我们从未见过的新面孔吗? {}".format(not True in results)) 
