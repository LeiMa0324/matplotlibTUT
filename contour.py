import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

'''
绘制等高线
'''

def f(x,y):
    #得到点的高度
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)

# 将两个x和y的数组返回坐标矩阵
# x 成为X的行向量，y成为Y的列向量，X和Y维数相等
X,Y = np.meshgrid(x,y)

# 把颜色fill进等高线内,8是等高线分位几个部分
plt.contourf(X,Y,f(X,Y),8,alpha = 0.75,cmap='hot')

# 绘制等高线，输入坐标XY和高度F(X,Y)
# 绘制8个高度的等高线
C= plt.contour(X,Y,f(X,Y),8,colors = 'black',linewidths=0.5)
# contour label 加上标签
plt.clabel(C,inline = True,fontsize =10)

# 删除x和y的ticks
plt.xticks(())
plt.yticks(())
plt.show()