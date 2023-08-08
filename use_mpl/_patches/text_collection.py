import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText, AnnotationBbox

fig, ax = plt.subplots()

# 创建文本集合
text1 = "Text 1"
text2 = "Text 2"
text3 = "Text 3"

texts = [text1, text2, text3]
positions = [(0.2, 0.5), (0.5, 0.5), (0.8, 0.5)]

for text, position in zip(texts, positions):
    # 创建文本框对象
    text_box = AnchoredText(text, loc='center', pad=0.2, borderpad=0.5, frameon=True)

    # 创建注释框
    ab = AnnotationBbox(text_box, position, xycoords='data', frameon=False)
    ax.add_artist(ab)

plt.axis('off')
plt.show()
