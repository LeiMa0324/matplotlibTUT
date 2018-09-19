import matplotlib.pyplot as plt
import numpy as np
'''
2.8 scatter 散点图
'''

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
# 每一组(x,y)得到一个T值，用于区分不同的颜色
T = np.arctan2(Y,X)
# 给color c 一个值，然后根据cmap映射到一个颜色上
plt.scatter(X,Y,s=75,c=T,alpha=0.5)
# 设置x和y轴的limit
plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))

# 隐藏所有ticks
plt.xticks(())
plt.yticks(())

plt.show()
