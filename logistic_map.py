import numpy as np
from matplotlib import pyplot as plt


def calc_y(x):
    n = x / 32
    n1 = r * n * (1 - n)
    return round(n1 * 32, 3)


x = range(1, 33)
ylist = [x]

for r in np.arange(3.0, 4.0, 0.1):
    r=round(r,1)
    y = []
    for i in x:
        y.append(calc_y(i))
    plt.plot(x, y, label='R='+str(r))
    ylist.append(y)

    pxs = []
    pys = []
    px = 2
    for c in range(256):
        py = calc_y(px)
        pxs.append(px)
        pys.append(py)
        px = py
    plt.plot(pxs, pys, "ob")
    print(pxs)
    print(pys)
    print("------------------------------")
plt.legend()
plt.show()


