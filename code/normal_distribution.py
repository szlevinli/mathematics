######################################################################
#
# 正态分布
#
######################################################################

import numpy as np
import matplotlib.pyplot as plt


def normal_pdf(x, sigma=1, mu=0):
    '''正态分布概率密度函数

        `pdf` is probability density function

        Parameter
        ---------
        sigma: float
            标准差 `standard deviation`
        mu: flaot
            平均值 `mean`
        x: float
            自变量
    '''
    normal = (1 / sigma * np.sqrt(2 * np.pi)
              ) ** -((x - mu) ** 2 / 2 * sigma ** 2)
    return normal


def main():
    sigma = 1
    mu = 0
    # 这里使用 linspace 而不是 arange 目的是让画出来图更加顺滑
    # x = np.arange(-3, 4)
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    ufunc = np.frompyfunc(normal_pdf, 3, 1)
    y = ufunc(x, sigma, mu)

    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    main()
