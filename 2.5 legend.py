import matplotlib.pyplot as plt
import numpy as np
'''
2.5 Legend 图例
修改坐标轴的位置
1. 给 plot 加上 label 标签
2.调用 plt.legend()
'''


x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure()

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('I am xlabel')
plt.ylabel('I am y')

new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1,22,4],
           [r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$'])

l1 = plt.plot(x,y2,label= 'up')
l2 = plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')
# 使用默认参数
# handles = [l1,l2,] 使用对象传入 legend
# labels 重新命名线的名字
# loc='best' 'upper right' ..等等
plt.legend(handles=[l1,],labels=['aaa',])

plt.show()