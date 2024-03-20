import numpy as np
from numpy import pi


def convert_elementwise(img):
    """
    将全景图像转换为鱼眼图
    """
    height, width, c = img.shape
    r0 = int(width / (2 * pi))
    d = r0 * 2
    cx, cy = r0, r0

    new_img = np.zeros((d, d, c), dtype=np.uint8)

    # 反推像素点对应原来图像的RBG颜色值
    for i in range(d):
        for j in range(d):
            r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2)

            if r > r0:
                continue  # 圆以外为黑色
            theta = np.arctan((j - cy) / (i - cx + 1e-10))
            if i < cx:
                theta = pi / 2 + theta
            else:
                theta = pi * 3 / 2 + theta
            xp = int(np.floor(theta / 2 / pi * width))
            yp = int(np.floor(r / r0 * (height // 1)) - 1)  # width除以2：只要图片的上一半
            new_img[j, i] = img[yp, xp]
    return new_img
