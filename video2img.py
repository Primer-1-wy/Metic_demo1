import os

import cv2

video_path = 'video/VID_20240721_174242_00_004.mp4'  # 视频地址
output_path = 'C:/Users/DELL/PycharmProjects/Metic_demo/img/test/'  # 输出文件夹
interval = 10  # 每间隔10帧取一张图片

def video_to_images(video_path, output_folder):
    num = 1
    vid = cv2.VideoCapture(video_path)
    frame_rate = vid.get(cv2.CAP_PROP_FPS)
    times=[]
    paths=[]
    while vid.isOpened():
        is_read, frame = vid.read()
        if is_read:
            if num % interval == 0:
                # 计算当前帧的时间戳（以秒为单位）
                current_time = num / frame_rate
                file_name = '%08d' % num
                # cv2.imwrite(output_path + str(file_name) + '.jpg', frame)
                # 00000111.jpg 代表第111帧
                cv2.waitKey(1)
                # print(current_time)
                # print(output_path + str(file_name) + '.jpg')
                times.append(current_time)
                paths.append(output_path + str(file_name) + '.jpg')
            num += 1
        else :
            break
    vid.release()
    return times,paths

if __name__ == '__main__':
    video_to_images(video_path,output_path)