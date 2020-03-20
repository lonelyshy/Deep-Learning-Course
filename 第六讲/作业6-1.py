import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "SimHei"  # 设置字体为宋黑
list1 = [[137.97, 145.00],
         [104.50, 110.00],
         [100.00, 93.00],
         [124.32, 116.00],
         [79.20, 65.32],
         [99.00, 104.00],
         [124.00, 118.00],
         [114.00, 91.00],
         [106.69, 62.00],
         [138.05, 133.00],
         [53.75, 51.00],
         [46.91, 45.00],
         [68.00, 78.50],
         [63.02, 69.65],
         [81.26, 75.69],
         [86.21, 95.30]
         ]

house_sell = np.array(list1)


def main():
    plt.scatter(house_sell[:, 0], house_sell[:, 1], color='red', marker='o')
    plt.title("商品房销售记录", fontsize=16, color='blue')
    plt.xlabel('面积(平方米)', fontsize = 14)
    plt.xlabel('价格(万元)', fontsize=14)
    plt.plot()
    plt.show()


if __name__ == '__main__':
    main()
