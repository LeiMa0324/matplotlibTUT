import matplotlib.pyplot as plt
import numpy as np

'''
2.9 bar 柱状图
'''

n = 12
X = np.arange(n)
# 向上的值Y1
Y1 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)
# 向下的值Y2
Y2 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)

# face color 主颜色，edgecolor 边框颜色
plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')

# 给每一个bar加上值
# zip()将对应的元素打包成一个元组，返回该元组的列表
for x,y in zip(X,Y1):
    # text的前两个参数表示text的位置，第三位是text文字
    # ha= horizontal alignment va = vertical alignment
    #.2f 代表保留两位小数
    plt.text(x+0.2,y+0.05,'%.2f'%y,ha='center',va='bottom')

for x,y in zip(X,Y2):
    plt.text(x+0.2,-y-0.05,'%.2f'%y,ha='center',va='top')


plt.xlim(-.5,n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())

plt.show()
