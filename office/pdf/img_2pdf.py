from PIL import Image, ExifTags
import os

# 使用较低分辨率的 A4 尺寸（例如 150 DPI）
A4_WIDTH, A4_HEIGHT = 1240, 1754  # A4 @ 150 DPI

def fix_image_orientation(img):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == "Orientation":
                break
        exif = img._getexif()
        if exif is not None:
            orientation_value = exif.get(orientation)
            if orientation_value == 3:
                img = img.rotate(180, expand=True)
            elif orientation_value == 6:
                img = img.rotate(270, expand=True)
            elif orientation_value == 8:
                img = img.rotate(90, expand=True)
    except Exception:
        pass
    return img

def convert_images_to_pdf(image_paths, output_pdf_path, quality=85):
    a4_images = []
    for path in image_paths:
        img = Image.open(path).convert("RGB")
        img = fix_image_orientation(img)

        if img.width > img.height:
            img = img.rotate(-90, expand=True)

        img.thumbnail((A4_WIDTH, A4_HEIGHT), Image.Resampling.LANCZOS)

        background = Image.new("RGB", (A4_WIDTH, A4_HEIGHT), (255, 255, 255))
        offset = ((A4_WIDTH - img.width) // 2, (A4_HEIGHT - img.height) // 2)
        background.paste(img, offset)

        a4_images.append(background)

    if a4_images:
        # 保存为 PDF 时进行 JPEG 压缩
        a4_images[0].save(
            output_pdf_path,
            save_all=True,
            append_images=a4_images[1:],
            resolution=150,  # 设置PDF输出分辨率
            quality=quality,
            optimize=True
        )
        print(f"✅ PDF 已压缩并保存: {output_pdf_path}")
    else:
        print("❌ 没有有效图片")

# 示例用法
image_folder = "image"
image_files = sorted([os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))])
output_pdf = "output_compressed.pdf"

convert_images_to_pdf(image_files, output_pdf)
