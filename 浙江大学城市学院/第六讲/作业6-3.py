import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import scale

df = pd.read_csv("boston.csv", header=0)
# 通过pandas导入波士顿数据集
ds = df.values
x_data = ds[:, :12]  # 前12列特征数据（0-11）
y_data = ds[:, 12]  # 第12列数据
train_num = 300  # 训练集的数目
vaild_num = 100  # 验证集的数目
test_num = len(x_data) - train_num - vaild_num  # 测试集的数目
# 训练集划分
x_train = x_data[:train_num]
y_train = y_data[:train_num]

# 验证集划分
x_valid = x_data[train_num:train_num + vaild_num]
y_valid = y_data[train_num:train_num + vaild_num]

# 测试集划分
x_test = x_data[train_num + vaild_num:train_num + vaild_num + test_num]
y_test = y_data[train_num + vaild_num:train_num + vaild_num + test_num]
# 转换数据类型
x_train = tf.cast(scale(x_train), dtype=tf.float32)
x_valid = tf.cast(scale(x_valid), dtype=tf.float32)
x_test = tf.cast(scale(x_test), dtype=tf.float32)

W = tf.Variable(tf.random.normal([12, 1], mean=0.0, stddev=1.0, dtype=tf.float32))
B = tf.Variable(tf.zeros(1), dtype=tf.float32)

training_epochs = 40  # 迭代次数
learning_rate = 0.001  # 学习率
batch_size = 10  # 批量训练一次的样本数


def loss(x, y, w, b):  # 定义损失函数
    err = model(x, w, b) - y  # 求模型预测值和标签值的差异
    squared_err = tf.square(err)  # 求平方，得出方差
    return tf.reduce_mean(squared_err)  # 求均值，得出均方差


def grad(x, y, w, b):
    with tf.GradientTape() as tape:
        loss_ = loss(x, y, w, b)
    return tape.gradient(loss_, [w, b])


optimizer = tf.keras.optimizers.SGD(learning_rate)


def model(x, w, b):  # 构建模型
    return tf.matmul(x, w) + b


def main():
    loss_list_train = []  # 训练集损失值
    loss_list_valid = []  # 验证集loss值
    total_step = int(train_num / batch_size)
    for epoch in range(training_epochs):
        for step in range(total_step):
            xs = x_train[step * batch_size:(step + 1) * batch_size, :]  # 每一轮取10个，12列
            ys = y_train[step * batch_size:(step + 1) * batch_size]

            grads = grad(xs, ys, W, B)
            optimizer.apply_gradients(zip(grads, [W, B]))  # 优化器根据梯度自动调整变量W和B

        loss_train = loss(x_train, y_train, W, B).numpy()
        loss_valid = loss(x_valid, y_valid, W, B).numpy()
        loss_list_train.append(loss_train)
        loss_list_valid.append(loss_valid)
        print("epoch = {:3d} ,train_loss={:.4f} ,valid_loss={:.4f}".format(epoch + 1, loss_train, loss_valid))
    loss_visual(loss_list_train,loss_list_valid)

def loss_visual(loss_list_train,loss_list_valid):
    plt.xlabel("Epchos")
    plt.ylabel("LOSS")
    plt.plot(loss_list_train,'blue',label="Train LOSS")
    plt.plot(loss_list_valid,"red",label = "Valid LOSS")
    plt.legend(loc = 1)
    plt.show()

if __name__ == '__main__':
    main()
