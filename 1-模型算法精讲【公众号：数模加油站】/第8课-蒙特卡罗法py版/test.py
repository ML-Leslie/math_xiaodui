import matplotlib.pyplot as plt
import numpy as np

# 创建x数据，从-10到10，每隔0.1一个点
x = np.arange(-10, 10, 0.1)

# 计算y数据
y1 = x
y2 = x**2

# 创建绘图窗口
plt.figure()
plt.title('1')
plt.xlabel('x')
plt.ylabel('y')
# 添加图例

# 绘制y = x的图像
plt.plot(x, y1, label='y = x')
# 显示图像
plt.legend()
plt.show()

plt.figure()
plt.title('2')
plt.xlabel('x')
plt.ylabel('y')
# 绘制y = x^2的图像

plt.plot(x, y2, label='y = x^2')

# 添加标题和标签
plt.legend()
# 显示图像
plt.show()
