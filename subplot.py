import numpy as np
import matplotlib.pyplot as plt



plt.figure()
plt.subplot(2,1,1)
plt.plot([0,1],[0,1])

# 第一张图片占了1-3的位置
plt.subplot(2,3,4)
plt.plot([0,1],[0,2])

plt.subplot(2,3,5)
plt.plot([0,1],[0,3])

plt.subplot(2,3,6)
plt.plot([0,1],[0,4])

plt.show()