import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    y = x > 0
    return y.astype(np.int32)


def step_function_v1(x):
    return np.array(x > 0, dtype=np.int32)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def identity_function(x):
    return x


x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # 指定y轴的范围
plt.show()

np.ndim(x) #维度
x.shape #形状
x.shape[0] #第一维度的形状