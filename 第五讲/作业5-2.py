import numpy as np

def main():
    x = [64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03]
    y = [62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 84.49, 127.44, 55.25, 104.84]
    x1 = np.array(x)#转化为矩阵
    y1 = np.array(y)
    px = x1.mean(dtype=np.float64)#x的均值  array.mean() 是求一个数组的均值
    py = y1.mean(dtype=np.float64)#y的均值
    w = (((x1 - px) * (y1 - py)).sum())/((((x1 - px)**2)).sum())
    #数组可以直接减一个数，其中所有元素都会减
    #数组和数组之间也可以直接相乘
    b = py - w*px
    print(w,"\n",b)











if __name__ == '__main__':
    main()