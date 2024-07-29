import torch
import torchvision
import numpy as np
import os
from pytorch_fid import fid_score

# 定义真实图像和生成图像的路径
real_images_folder = 'D:/temp/1'
generated_images_folder = 'D:/temp/2'

# 计算 FID 值
fid_value = fid_score.calculate_fid_given_paths(
    [real_images_folder, generated_images_folder],
    batch_size=9,
    device='cuda:0',  # 使用 GPU 或 'cpu'
    dims=2048
)

print(f'FID Value: {fid_value}')
