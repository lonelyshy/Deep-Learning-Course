import numpy as np

def main():

    a = int(input("请输入一个1-100之间的整数:"))
    np.random.seed(612)#设置随机数种子
    r1 = np.random.rand(1000)#生成一个[0,1)之间均匀分布的随机数数组，包含1000个元素
    index = []
    for b in range(1000):#循环计算出可以被输入整数整除的数字
        if b%a == 0:
            index.append(b)
    num = 1
    print("序号 索引值 随机数")
    for c in index:
        print("{}\t{}\t{}".format(num,c,r1[c]))
        num = num +1





if __name__ == '__main__':
    main()





