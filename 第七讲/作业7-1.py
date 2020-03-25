import matplotlib.pyplot as plt
from PIL import Image
import tensorflow as tf
import numpy as np

plt.rcParams["font.family"] = "SimHei"  # 如果画图中出现中文 需要设置字体为宋黑


def main():
    img = Image.open('test.png')
    assert isinstance(img, Image.Image)  # 断言判断img是不是Image.Image类型 此举是为了告诉pycharm是这种类型 然后可以有代码补全
    img_r, img_g, img_b = img.split()
    plt.figure(figsize=(10, 10))
    plt.suptitle('图像基本操作', color='blue', fontsize=20)
    plt.subplot(221)
    plt.axis('off')  # 关闭xy轴和标签
    img_small = img_r.resize((50, 50))
    plt.imshow(img_small, cmap='gray')
    plt.title('R-缩放', fontsize=14)

    plt.subplot(222)
    img2 = img_g.resize((250, 250))
    img2 = img2.convert('L')
    img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)  # 水平翻转
    img2 = img2.transpose(Image.ROTATE_270)  # 在顺时针90度  就是逆时针270度
    plt.axis([0, 250, 250, 0])
    plt.imshow(img2, cmap='gray')
    plt.title('G-镜像+旋转', fontsize=14)

    plt.subplot(223)
    plt.axis('off')

    img_crop = img_b.resize((250, 250)).crop((0, 0, 150, 150))
    plt.imshow(img_crop, cmap='gray')
    plt.title('B-裁剪', fontsize=14)

    plt.subplot(224)
    plt.axis('off')
    img_new = Image.merge('RGB', [img_r, img_g, img_b])
    plt.imshow(img_new)
    plt.title(img_new.mode, fontsize=14)
    plt.tight_layout(rect=[0, 0, 1, 0.9])  # 自动调整每个子图的位置，不会让标题重叠
    plt.show()


if __name__ == '__main__':
    main()
