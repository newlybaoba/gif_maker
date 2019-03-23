# -*- coding:utf-8 -*-
# Author : Niuli
# Data : 2018/11/12 下午5:07
import os
import re

pic_list = os.listdir()
pic_type = ['png', 'jpg', 'jpeg', 'bmp']
image_list = []
print(pic_list)

for p in pic_list:
    for pt in pic_type:
        if pt in p:
            image_list.append(p)


image_list.sort(key=lambda i: int(re.match(r'(\d+)', i).group()))

print(image_list)
