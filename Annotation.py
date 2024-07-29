import os

import numpy as np

import video2img
import GetCameraParam

video_path = 'video/VID_20240721_174242_00_004.mp4'  # 视频地址
output_path = 'C:/Users/DELL/PycharmProjects/Metic_demo/img/test/'  # 输出文件夹

def getImgName(filePath):
    img_name = os.listdir(filePath)

if __name__ == "__main__":
    filePath = 'img/test'
    # img_paths=[]
    RT = GetCameraParam.getRT(filePath)
    time,path=video2img.video_to_images(video_path,output_path)
    time=np.array(time).reshape(-1,1)
    path=np.array(path).reshape(-1,1)

    annotation=np.hstack((time,path,RT))
    print(annotation)
    n=annotation.shape[0]
    m=annotation.shape[1]
    # # print(RT[n-1])
    # for i in range(n):
    #     for j in range(m):
    #         print(str(RT[i][j])+' ')
    #     print("\n")
    # 指定文件名和打开模式
    file_name = 'example.txt'
    mode = 'w'
    # 打开文件
    with open(file_name, mode) as file:
        # 写入多行数据
        for i in range(n):
            for j in range(m):
                file.write(str(annotation[i][j])+' ')
            file.write("\n")
    # 文件在 with 语句块结束时自动关闭