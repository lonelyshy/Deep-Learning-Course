import matplotlib.pyplot as plt
from PIL import Image
import tensorflow as tf
import numpy as np
plt.rcParams["font.family"] = "SimHei"  # 如果画图中出现中文 需要设置字体为宋黑

def main():
    mnist = tf.keras.datasets.mnist#加载mnist数据集
    (train_x,train_y),(test_x,test_y) = mnist.load_data()
    a = 0
    for i in range(16):
        num = np.random.randint(0,50000)
        plt.subplot(4,4,a+1)
        plt.axis('off')#关闭坐标轴
        plt.imshow(train_x[num],cmap='gray')
        plt.title('标签值:'+str(train_y[num]),fontsize = 14)
        a = a + 1
    plt.suptitle('MNIST测试集样本',color = 'red',fontsize = 20)
    plt.tight_layout(rect=[0, 0, 1, 0.9])
    plt.show()

if __name__ == '__main__':
    main()