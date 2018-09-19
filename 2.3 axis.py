import matplotlib.pyplot as plt
import numpy as np
'''
2.3 设置坐标轴1
修改坐标轴标尺，名称和限定范围
一个图像窗口中的一个图像为 axes
'''
# 设置 x 的取值范围
plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('I am X')
plt.ylabel('I am y')

# ticks 是坐标轴上的标记
new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3],
           # 用$$转换成数学模式字体
           #转置符+alpha 打印为数学符号 \alpha
           [r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])



'''
2.4 设置坐标轴2
修改坐标轴的位置
'''
# gca = get current axis 获取当前 axis
ax = plt.gca()
# 将当前axis 的上，右边框去掉，因为下边和左边的边框分别要放置 x 轴和 y 轴
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 将 x 轴和 y 轴放置在下边框和左边框上
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# 将 x 轴绑定在 y 轴0的位置,'data'标志后面的参数是以数据为单位
ax.spines['bottom'].set_position(('data',0))
# 将 y 轴绑定在 x 轴0的位置
ax.spines['left'].set_position(('data',0))