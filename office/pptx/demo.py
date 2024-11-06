import re

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Inches
from pptx.util import Pt


def replace_text_in_ppt_with_style(ppt_path, pattern, replacement_text, color=(255, 0, 0)):
    """
    在PPT中查找并替换所有匹配指定模式的文本，并将新文本设置为指定颜色。

    :param ppt_path: str, 输入的PPT文件路径
    :param pattern: str, 要匹配的正则表达式模式
    :param replacement_text: str, 替换后的文本内容
    :param color: tuple, RGB颜色值，默认为红色 (255, 0, 0)
    """
    # 打开PPT文件
    prs = Presentation(ppt_path)

    # 遍历幻灯片和文本框
    for slide in prs.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                # 遍历每一段文字
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        # 如果找到匹配的文本，则进行替换
                        if re.search(pattern, run.text):
                            # 将文本替换为新的文本内容
                            run.text = re.sub(pattern, replacement_text, run.text)
                            # 设置字体颜色为指定颜色
                            run.font.color.rgb = RGBColor(*color)
                            # 其他样式设置可以在此添加，如字体大小等
                            run.font.size = Pt(18)  # 设置字体大小为18号字，可根据需要调整

    # 保存修改后的PPT
    modified_ppt_path = ppt_path.replace(".pptx", "_text_modified.pptx")
    prs.save(modified_ppt_path)
    print(f"替换并设置样式完成，保存到文件: {modified_ppt_path}")
    return modified_ppt_path


def insert_image_in_ppt(ppt_path, slide_index, image_path, left, top, width=None, height=None):
    """
    在指定幻灯片的给定位置插入图片。

    :param ppt_path: str, 输入的PPT文件路径
    :param slide_index: int, 插入图片的幻灯片编号（从0开始）
    :param image_path: str, 图片文件路径
    :param left: float, 图片左边距（以英寸为单位）
    :param top: float, 图片上边距（以英寸为单位）
    :param width: float, 图片宽度（可选，以英寸为单位）
    :param height: float, 图片高度（可选，以英寸为单位）
    """
    # 打开PPT文件
    prs = Presentation(ppt_path)

    # 确认幻灯片编号在有效范围内
    if slide_index < 0 or slide_index >= len(prs.slides):
        print("幻灯片编号超出范围")
        return

    # 获取指定的幻灯片
    slide = prs.slides[slide_index]

    # 插入图片
    if width and height:
        slide.shapes.add_picture(image_path, Inches(left), Inches(top), width=Inches(width), height=Inches(height))
    else:
        slide.shapes.add_picture(image_path, Inches(left), Inches(top))

    # 保存修改后的PPT
    modified_ppt_path = ppt_path.replace(".pptx", "_with_image.pptx")
    prs.save(modified_ppt_path)
    print(f"图片插入完成，保存到文件: {modified_ppt_path}")
    return modified_ppt_path


def demo():
    # 示例用法
    ppt_path = 'example.pptx'  # 输入的PPT路径
    pattern = r'旧文本'  # 要匹配的模式（可以是正则表达式）
    replacement_text = '新文本'  # 替换后的文本内容
    color = (255, 0, 0)  # 红色

    # 执行替换操作
    slide_index = 2  # 要插入图片的幻灯片编号，从0开始
    image_path = 'image.jpg'  # 插入的图片路径
    left, top = 1, 1  # 图片插入位置的左、上边距，以英寸为单位
    width, height = 2, 2  # 图片宽度和高度，以英寸为单位

    # 执行替换和插入操作
    replace_text_in_ppt_with_style(ppt_path, pattern, replacement_text, color)
    insert_image_in_ppt(ppt_path, slide_index, image_path, left, top, width, height)


if __name__ == '__main__':
    demo()