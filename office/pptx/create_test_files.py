from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN


def create_test_ppt(ppt_path='example.pptx'):
    # 创建一个空的PPT文件
    prs = Presentation()

    # 添加第一张幻灯片并设置标题和内容
    slide_1 = prs.slides.add_slide(prs.slide_layouts[0])  # 使用带标题的布局
    title = slide_1.shapes.title
    subtitle = slide_1.placeholders[1]

    title.text = "测试PPT生成"
    subtitle.text = "这是一个用于测试的PPT文件"

    # 添加第二张幻灯片，包含一些文本和可替换的占位符
    slide_2 = prs.slides.add_slide(prs.slide_layouts[1])  # 使用带标题和内容的布局
    title = slide_2.shapes.title
    title.text = "替换测试幻灯片"

    # 添加一些占位符文本
    textbox = slide_2.shapes.add_textbox(Inches(1), Inches(2), Inches(8), Inches(1))
    textbox.text_frame.text = "这是一个包含旧文本的段落，用于替换测试。"
    p = textbox.text_frame.add_paragraph()
    p.text = "这里也有一个旧文本。"
    p.font.size = Pt(18)
    p.alignment = PP_ALIGN.LEFT

    # 添加第三张幻灯片，用于测试图片插入
    slide_3 = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide_3.shapes.title
    title.text = "图片插入测试幻灯片"

    textbox = slide_3.shapes.add_textbox(Inches(1), Inches(2), Inches(8), Inches(1))
    textbox.text_frame.text = "图片将在这里插入，左上角位置为 (1, 3) 英寸。"

    # 保存生成的PPT
    prs.save(ppt_path)
    print(f"测试PPT文件已保存到 {ppt_path}")


if __name__ == '__main__':
    # 调用函数生成测试PPT
    create_test_ppt()
