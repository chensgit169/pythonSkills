import cv2
import mediapipe as mp
import numpy as np


def replace_background_with_mediapipe(image_path, output_path, background_color=(0, 0, 0)):
    # 初始化 Mediapipe 的 Selfie Segmentation
    mp_selfie_segmentation = mp.solutions.selfie_segmentation.SelfieSegmentation(model_selection=1)

    # 读取输入图像
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 获取分割结果
    results = mp_selfie_segmentation.process(image_rgb)
    mask = results.segmentation_mask > 0.5  # 生成二值掩码

    # 创建背景
    background = np.full_like(image, background_color)

    # 合并前景与新背景
    output_image = np.where(mask[..., None], image, background)

    # 保存结果
    cv2.imwrite(output_path, output_image)
    print(f"替换后的图片保存到: {output_path}")


# 调用函数
replace_background_with_mediapipe("input.jpg", "output.jpg", background_color=(255, 255, 255))  # 白色背景
