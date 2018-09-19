import numpy as np
import matplotlib.pyplot as plt

a = np.array([0.31,0.36,0.42,
              0.36,0.43,0.52,
              0.42,0.52,0.65]).reshape(3,3)

plt.imshow(a,
           #图片色块变化
           #https://matplotlib.org/gallery/images_contours_and_fields/interpolation_methods.html?highlight=interpolation
           interpolation ='nearest',
           cmap='bone',
           # 决定数据展示的顺序'lower''upper'
           origin='upper')
# 添加颜色标注
# 将标注压缩到90%大小
plt.colorbar(shrink = 0.9)

plt.xticks(())
plt.yticks(())
plt.show()