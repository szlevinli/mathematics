######################################################################
#
# 正态分布
#   用 scipy 函数库自带的正态分布密度函数
#
######################################################################

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def main():
    sigma = 1  # standard deviation
    mu = 0  # mean
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    y = norm.pdf(x, )

    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    main()
