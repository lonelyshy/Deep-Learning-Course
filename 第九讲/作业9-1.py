import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def main():
    x1 = np.array([137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00, 114.00,
                   106.69, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26, 86.21])
    x2 = np.array([3, 2, 2, 3, 1, 2, 3, 2, 2, 3, 1, 1, 1, 1, 2, 2])
    y = np.array([145.00, 110.00, 93.00, 116.00, 65.32, 104.00, 118.00, 91.00,
                  62.00, 133.00, 51.00, 45.00, 78.50, 69.65, 75.69, 95.30])
    tx1 = tf.constant(x1,dtype = tf.float64,shape = (16,1))
    tx2 = tf.constant(x2,dtype = tf.float64,shape = (16,1))
    y = tf.constant(y,dtype = tf.float64,shape = (16,1))
    tone = tf.ones([16,1],dtype = tf.float64)
    X = tf.concat([tone,tx1,tx2],axis = 1)#拼接张量
    Xt = tf.transpose(X) #计算X转置
    XtX_1 = tf.linalg.inv(tf.matmul(Xt,X))
    XtX_1_Xt = tf.matmul(XtX_1,Xt)
    W = tf.matmul(XtX_1_Xt,y)
    W = (tf.reshape(W,shape = (3,1))).numpy()
    print('请输入商品房面积和房间数')
    x1_test = float(input('面积(20-500之间的实数): '))
    x2_test = int(input('房间数(1-10之间的整数): '))
    y_pred = float(W[1]*x1_test+W[2]*x2_test +W[0])
    print('预测价格{} 万元'.format(round(y_pred,2)))



if __name__ == '__main__':
    main()
