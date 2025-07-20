import cv2
import os

# 输入视频路径
video_path = "Problem.mp4"  # 替换为你的视频文件路径
output_folder = "output_frames"  # 输出截图文件夹

# 创建输出文件夹
os.makedirs(output_folder, exist_ok=True)

# 打开视频文件
cap = cv2.VideoCapture(video_path)

# 检查视频是否成功打开
if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

# 获取视频信息
fps = cap.get(cv2.CAP_PROP_FPS)  # 每秒帧数
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 总帧数
print(f"Video FPS: {fps}, Total Frames: {frame_count}")

# 逐帧读取视频
frame_index = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break  # 视频读取结束

    # 保存当前帧为图像
    frame_filename = os.path.join(output_folder, f"frame_{frame_index:04d}.png")
    cv2.imwrite(frame_filename, frame)
    print(f"Saved {frame_filename}")

    frame_index += 1

# 释放资源
cap.release()
print("Video processing complete!")
