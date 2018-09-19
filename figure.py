import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y1 = 2*x+1
y2 = x**2
'''
2.2 figure 图像
一个 figure 为一个图片窗口
'''

#定义第一个 figure
plt.figure()
plt.plot(x,y1)

#定义第二个 figure
# num figure 的号码，figsize 为 fig 的大小
plt.figure(num=3,figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')




