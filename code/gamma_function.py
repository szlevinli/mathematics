######################################################################
#
# 通过图表方式理解数学中的 gamma function
#
######################################################################

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial

def main():
    x = np.arange(1, 5)
    y = factorial(x)

    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    main()
