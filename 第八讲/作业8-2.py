import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def main():
    x = np.array([64.3,99.6,145.45,63.75, 135.46, 92.85, 86.97, 144.76, 59.3,116.03])
    y = np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
    tx = tf.constant(x,dtype = tf.float64)
    ty = tf.constant(y,dtype = tf.float64)

    w = (
            ((x.size*(tf.reduce_sum(tx*ty))) -(tf.reduce_sum(tx)*tf.reduce_sum(ty)) )/
         ((x.size*(tf.reduce_sum(tx**2) - (tf.reduce_sum(tx))**2)))
    )

    b = (
            (tf.reduce_sum(ty) - w*(tf.reduce_sum(tx)))/
         x.size
    )
    print('w = {}'.format(w))
    print('b = {}'.format(b))




if __name__ == '__main__':
    main()