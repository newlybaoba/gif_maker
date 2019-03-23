import os
import re

import imageio

pic_list = os.listdir()
pic_type = ['png', 'jpg', 'jpeg', 'bmp']


def create_gif(image_list, gif_name, duration):
    """
    gif_name ： 字符串，所生成的 gif 文件名，带 .gif 后缀
    path :     需要合成为 gif 的图片所在路径
    duration :  gif 图像时间间隔
    """

    frames = []
    # 把图片 append 进列表
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # 保存为 gif 图
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)

    return


def main():
    # -------- 获取要拼合的图片列表 -------
    image_list = []

    for p in pic_list:
        for pt in pic_type:
            if pt in p:
                image_list.append(p)

    image_list.sort(key=lambda i: int(re.match(r'(\d+)', i).group()))
    print(image_list)

    # --------- 生成gif图片名称 ---------
    gif_name = 'new.gif'

    # --------- 变换时间 -------
    duration = 1
    create_gif(image_list, gif_name, duration)


if __name__ == "__main__":
    main()
