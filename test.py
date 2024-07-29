import os
import video2img
import numpy as np
video_path = 'video/VID_20240721_174242_00_004.mp4'  # 视频地址
output_path = 'C:/Users/DELL/PycharmProjects/Metic_demo/img/test/'  # 输出文件夹
def getImgName(filePath):
    return os.listdir(filePath)


print(video2img.video_to_images(video_path,output_path))