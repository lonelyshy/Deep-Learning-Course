import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

plt.rcParams["font.family"] = "SimHei"  # 设置字体为宋黑
boston_housing = tf.keras.datasets.boston_housing
(train_x, train_y), (_, _) = boston_housing.load_data(test_split=0)#加载数据集
boston_housing_attribute = ['CRIM', 'ZN', 'INdus', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B',
                            'LSTAT']#设置各个标题的属性


# 波士顿放假数据集前13个属性
def boston_all():#这个是显示所有表
    plt.figure('boston_housing', figsize=(14, 14))
    plt.suptitle('各个属性与房价之间的关系')
    index_x = 1

    for a in boston_housing_attribute:
        plt.subplot(4,4,index_x)#划分子图
        plt.title(index_x.__str__()+'.'+a+'-'+'Price')
        plt.scatter(train_x[:,index_x - 1],train_y,marker= 'o',color = 'blue')#绘制散点图
        plt.xlabel(a)#设置子图x坐标轴
        plt.ylabel('price($1000\'s)')#设置子图y坐标轴
        index_x = index_x + 1
    plt.tight_layout(rect=[0,0,1,0.9])#自动调整每个子图的位置，不会让标题重叠

def boston_one(sx):#这个是显示指定的表
    for a in boston_housing_attribute:
        print('{} -- {}'.format(boston_housing_attribute.index(a) + 1, a))
    plt.figure('one', figsize=(5, 5))
    plt.scatter(train_x[:,sx - 1],train_y,marker= 'o',color = 'lightblue')
    plt.xlabel(boston_housing_attribute[sx-1])
    plt.ylabel('price($1000\'s)')
    plt.title(sx.__str__()+'.'+boston_housing_attribute[sx-1]+'-'+'Price')

def main():

    boston_all()
    sx = int(input('请选择属性:'))
    boston_one(sx)
    plt.plot()
    plt.show()


if __name__ == '__main__':
    main()
