import math

def main():
    try:
        a,b,c=input('请输入与abc 用空格分开:').split()
    except ValueError:
        print("数值输入多了或者少了")
        return 
    #同时输入多个数值空格间隔，输入的是字符串
    a,b,c = map(eval,[a,b,c])
    #用map函数 将字符串转换为数字
    d = math.pow(b,2) - (4*a*c)
    e = 0
    if d > 0:
        print("{}x²+{}x+{} = 0 有两个不相等的实数根".format(a,b,c))
        e = 1
    elif d == 0:
        print("{}x²+{}x+{} = 0 有两个相等的实数根".format(a,b,c))
        e = 2
    else:
        print("{}x²+{}x+{} = 0 有没有的实数根".format(a,b,c))

    if e == 1:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
        print("x1 = {},x2 = {}".format(x1,x2))
    elif e == 2:
        x1 = (-b+math.sqrt(d))/(2*a)
        print("x = {}".format(x1))

if __name__ == "__main__":
    main()

