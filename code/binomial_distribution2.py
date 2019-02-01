######################################################################
#
# 二项式分布
#   用 scipy 函数库自带的二项式分布质量函数
#
######################################################################

import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt


def main():
    n = 40 # 试验的次数
    p = 0.5 # 单次试验成功的概率
    k = np.linspace(1, n, 100) # 40次试验中成功的次数从1到n
    y = binom.pmf(k, n, p)

    plt.plot(k, y)
    plt.show()


if __name__ == '__main__':
    main()
