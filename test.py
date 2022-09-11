
import matplotlib.pyplot as plt

from PIL import Image

img1 = Image.open('./bg.jpg')

img2 = Image.open('./bg.jpg')

#结果展示

plt.rcParams['font.sans-serif'] = ['SimHei'] # 中文乱码

plt.subplot(121)

plt.imshow(img1)

plt.title('图像1')

#不显示坐标轴

plt.axis('off')

#子图2

plt.subplot(122)

plt.imshow(img2)

plt.title('图像2')

plt.axis('off')

# #设置子图默认的间距

plt.tight_layout()

#显示图像

plt.show()