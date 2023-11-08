import imageio
from pyppeteer import launch

async def capture_screenshot(url):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)

    # 获取页面的尺寸
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio
        }
    }''')

    # 设置页面视口大小
    await page.setViewport(dimensions)

    # 等待动画加载完成（可根据具体情况调整等待时间）
    await asyncio.sleep(2)

    # 获取页面的帧数
    frames_count = await page.evaluate('''() => {
        return document.querySelector('body').getElementsByTagName('img').length;
    }''')

    # 逐帧截图并保存为临时文件
    for i in range(frames_count):
        await page.evaluate('''() => {
            document.querySelector('body').getElementsByTagName('img')[arguments[0]].style.display = 'none';
        }''', i)
        screenshot = await page.screenshot()
        imageio.imwrite(f'frame_{i}.png', screenshot)

    await browser.close()

# 设置HTML文件路径
url = "file:///path/to/your_html_file.html"  # 替换为你的HTML文件路径

# 异步执行截图
asyncio.get_event_loop().run_until_complete(capture_screenshot(url))

# 合成图像帧为GIF
frames = []
for i in range(frames_count):
    frames.append(imageio.imread(f'frame_{i}.png'))

output_file = "animation.gif"  # 输出GIF图片路径
imageio.mimsave(output_file, frames, format='GIF', duration=0.2)

# 删除临时文件
for i in range(frames_count):
    os.remove(f'frame_{i}.png')
