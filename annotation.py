import matplotlib.pyplot as plt
import numpy as np


'''
2.6 annotation 标注
1. 标注图中的一个点(使用 scatter)
2. 给图片加上 text 备注
'''


x = np.linspace(-3,3,50)
y = 2*x+1

plt.figure(num=1,figsize=(8,5),)
plt.plot(x,y)

ax = plt.gca()
# 将右，上边框隐藏
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 将 x 轴设置在 bottom 边框上
ax.xaxis.set_ticks_position('bottom')
# 将bottom 边框绑定在 y 轴的0位置（将 x 轴移到图像中间）
ax.spines['bottom'].set_position(('data',0))
# 将 y 轴设置在 left 边框上
ax.yaxis.set_ticks_position('left')
# 将 left 边框绑定在 x 轴的0位置（将 y 轴移到图像中间）
ax.spines['left'].set_position(('data',0))

# 添加标注点
x0 = 1
y0 = 2*x0 + 1
# 使用 scatter画一个点,s=size
plt.scatter(x0,y0,s=50,color='b')
# 绘制从(x0,y0)到(x0,0)的虚线
plt.plot([x0,x0],[y0,0],'k--',linewidth = 2.5)

# method 1 使用 plt.annotate
            # annotation 的文字内容
plt.annotate(r'$2x+1=%s$'% y0,
# 在 xy=(x0,y0)出打印 string，xycoords='data' 意思为以 data 为基准
             xy=(x0,y0),xycoords='data',
            # 使用 textcoords='offset points' 代表偏置点为 xy 的(+30,-30)的地方放置 text
             xytext=(+30,-30),
             textcoords='offset points',
             fontsize=16,
             # 箭头形状，弧度等
             arrowprops= dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))

# method 2 使用 plt.text
# 开始位置
plt.text(-3.7,3,r'$This\ is\ some\ text.\ \mu\ \sigma_i\ \alpha_t $',
         fontdict={'size':16,'color':'r'})

plt.show()
