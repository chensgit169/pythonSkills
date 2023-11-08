import os

import cv2
import numpy as np
from numpy import pi

# 路径(文件夹)
input_path = 'panorama'
output_path = 'fisheye'
os.makedirs(output_path, exist_ok=True)


def convert(img, upper_ratio: float = 1.):
    """
    将全景图像转换为鱼眼图，运算经过了向量化并行。
    
    Args:
        img: ndarray, shape=(height, width, c)
        upper_ratio: float, default=1. 保留图像上半部分的比例，例如k=2/3保留图像的上2/3部分，范围 0~1.0
    """
    height, width, c = img.shape
    r0 = int(width / (2 * pi))
    d = r0 * 2
    cx, cy = r0, r0

    new_img = np.zeros((d, d, c), dtype=np.uint8)
    ixiy = np.meshgrid(np.arange(d), np.arange(d))
    ix, iy = ixiy

    # 极坐标
    rs = np.sqrt((ix - cx) ** 2 + (iy - cy) ** 2)
    thetas = pi/2 + np.arctan((iy - cy) / (ix - cx + 1e-10))
    thetas[ix >= cx] += pi

    # 反推像素点对应原来图像的RBG颜色值
    xps = np.floor(thetas / (2 * pi) * width)
    yps = np.floor(rs / r0 * (height * upper_ratio)) - 1

    # 遍历赋值
    for i in range(d):
        for j in range(d):
            r = rs[i, j]
            if r > r0:
                continue  # 圆以外为黑色
            xp = int(xps[j, i])
            yp = int(yps[j, i])
            new_img[j, i] = img[yp, xp]
    return new_img


def main(upper_ratio: float = 1.):
    """
    遍历文件夹中的全景图像，将其转换为鱼眼图像并保存到指定文件夹中。
    """
    for file in os.listdir(input_path):
        img_in = cv2.imread(os.path.join(input_path, file))  # 像素RBG值阵列
        img_out = convert(img_in, upper_ratio)
        cv2.imwrite(os.path.join(output_path, file), img_out)
        print(file, 'done')


if __name__ == '__main__':
    # 参数文件
    # arg_file = './upper_ratio.txt'
    # if os.path.exists(arg_file):
    #     upper_ratio = float(open(arg_file, 'r').read().strip())
    # else:
    #     upper_ratio = 1.0
    # print('upper_ratio=', upper_ratio)

    main(upper_ratio=1.0)
