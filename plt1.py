import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(-1,1,50)
# y1 = 2*x+1
# y2 = x**2
# '''
# 2.2 figure 图像
# 一个 figure 为一个图片窗口
# '''
#
# #定义第一个 figure
# plt.figure()
# plt.plot(x,y1)
#
# #定义第二个 figure
# # num figure 的号码，figsize 为 fig 的大小
# plt.figure(num=3,figsize=(8,5))
# plt.plot(x,y2)
# plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
#
#
# '''
# 2.3 设置坐标轴1
# 修改坐标轴标尺，名称和限定范围
# 一个图像窗口中的一个图像为 axes
# '''
# # 设置 x 的取值范围
# plt.xlim((-1,2))
# plt.ylim((-2,3))
# plt.xlabel('I am X')
# plt.ylabel('I am y')
#
# # ticks 是坐标轴上的标记
# new_ticks = np.linspace(-1,2,5)
# plt.xticks(new_ticks)
# plt.yticks([-2,-1.8,-1,1.22,3],
#            # 用$$转换成数学模式字体
#            #转置符+alpha 打印为数学符号 \alpha
#            [r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])
#
#
#
# '''
# 2.4 设置坐标轴2
# 修改坐标轴的位置
# '''
# # gca = get current axis 获取当前 axis
# ax = plt.gca()
# # 将当前axis 的上，右边框去掉，因为下边和左边的边框分别要放置 x 轴和 y 轴
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
#
# # 将 x 轴和 y 轴放置在下边框和左边框上
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
#
# # 将 x 轴绑定在 y 轴0的位置,'data'标志后面的参数是以数据为单位
# ax.spines['bottom'].set_position(('data',0))
# # 将 y 轴绑定在 x 轴0的位置
# ax.spines['left'].set_position(('data',0))

'''
2.5 Legend 图例
修改坐标轴的位置
1. 给 plot 加上 label 标签
2.调用 plt.legend()
'''

#
# x = np.linspace(-3,3,50)
# y1 = 2*x+1
# y2 = x**2
#
# plt.figure()
#
# plt.xlim((-1,2))
# plt.ylim((-2,3))
# plt.xlabel('I am xlabel')
# plt.ylabel('I am y')
#
# new_ticks = np.linspace(-1,2,5)
# plt.xticks(new_ticks)
# plt.yticks([-2,-1.8,-1,1,22,4],
#            [r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$'])
#
# l1 = plt.plot(x,y2,label= 'up')
# l2 = plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')
# # 使用默认参数
# # handles = [l1,l2,] 使用对象传入 legend
# # labels 重新命名线的名字
# # loc='best' 'upper right' ..等等
# plt.legend(handles=[l1,],labels=['aaa',])
#
# plt.show()

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
# 使用 scatter画一个点
plt.scatter(x0,y0)

plt.show()



