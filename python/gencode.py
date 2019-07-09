#!/usr/bin/env python
#coding:utf8
import random
import os
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO

font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "font.ttf")

def GenPic():
    img1 = Image.new(mode="RGB", size=(120,30), color=(255,255,255))
    draw1 = ImageDraw.Draw(img1, mode="RGB")
    font1 = ImageFont.truetype(font_path, 28)
    checkcode = ""

    for i in range(4):
        char1=random.choice([chr(random.randint(65,78)), chr(random.randint(80,90)), str(random.randint(1,9))])
        checkcode += char1
        color1=(random.randint(10,255), random.randint(10,255), random.randint(10,255))
        draw1.text([6+i*30,0], char1, color1, font = font1)

    f = BytesIO()
    img1.save(f, format="jpeg")
    f.seek(0)
    return checkcode.lower(), f
    


if __name__ == "__main__":
    GenPic()
    img1.show()

#c,f = GenPic()
#print c
#print f.read()
