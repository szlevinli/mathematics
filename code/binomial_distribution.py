######################################################################
#
# 二项式分布
#
######################################################################

import numpy as np
import scipy.special as spec
import matplotlib.pyplot as plt


def bd_pmf(n, p, k):
    """二项式的概率质量函数

        Parameters
        ----------
        n：int
            试验的次数
        p：float
            试验成功的概率。比如在骰子问题中，投到4的概率就是1/6
        k：int
            成功次数

        Returns
        ------
        val: int, float
            返回成功k次的概率
    """
    return spec.comb(n, k) * p ** k * (1 - p) ** (n - k)


def main():
    # 以下列子的意思是：
    #   拿一个公平的骰子，投10次，得到4的次数从1到10的概率

    n = 10   # 试验次数
    p = 1/6  # 成功概率。以骰子为例，得到任一一个指定面比如4的概率

    x = np.arange(1, n+1)
    y = np.zeros(n)

    # 使用 `numpy` 提供的 `frompyfunc` 函数创建一个自定义 `Universal Function` 简称 `ufunc`
    # `ufunc`的功能是自动迭代 `ndarray` 中的元素应用于指定的函数，从而避免手工编写迭代代码
    test_ufunc = np.frompyfunc(bd_pmf, 3, 1)
    y = test_ufunc(n, p, x)
    print(y)

    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    main()
