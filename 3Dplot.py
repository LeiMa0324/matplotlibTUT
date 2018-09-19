import matplotlib.pyplot as plt
import numpy as np
# 引入3d坐标轴
from  mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
# 在figure上加上3D的axes
ax = Axes3D(fig)

# X,Y value

X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)

# 定义坐标矩阵
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X**2+Y**2)
Z = np.sin(R)

# 绘制3D曲面
# rstride = row stride 行间隔 cstride = column stride 列跨度
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='rainbow')
# 绘制底面等高线
# zdir 代表从哪个轴映射到平面上,offset 代表压到z=-2的平面上
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')

ax.set_zlim(-2,2)
plt.show()