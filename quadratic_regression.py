import matplotlib.pyplot as plt
import math
import numpy as np
from numpy import random

def takeY(x: float, a: float, b: float, c: float, noise: float = False) -> float:

    y = (a*math.pow(x, 2) + b*x + c)

    if noise:
        return random.normal(loc=y, scale=0.3)
    else:
        return y

def main():
    yPositions = []
    iterations = []

    x = 0
    step = 0.01
    while x <= 3:
        yPositions.append(takeY(x, -1, 15, 0, True))
        iterations.append(x)
        x+=step

    y_array = np.array(yPositions)
    x_array = np.array(iterations)

    mean_x = x_array.mean()
    mean_x2 = np.array(x_array * x_array).mean()
    mean_y = y_array.mean()

    x_minus_mean = np.array(x_array - mean_x)
    y_minus_mean = np.array(y_array - mean_y)
    x2_minus_mean = np.array(np.array(x_array * x_array) - mean_x2)

    sxx = np.array(x_minus_mean * x_minus_mean).sum()
    sxy = np.array(x_minus_mean * y_minus_mean).sum()
    sxx2 = np.array(x_minus_mean * x2_minus_mean).sum()
    sx2x2 = np.array(x2_minus_mean * x2_minus_mean).sum()
    sx2y = np.array(x2_minus_mean * y_minus_mean).sum()

    calc_b = (sxy * sx2x2 - sx2y * sxx2) / (sxx * sx2x2 - (sxx2 * sxx2))

    calc_a = (sx2y*sxx - sxy*sxx2) / (sxx*sx2x2 - (sxx2 * sxx2))

    calc_c = mean_y - calc_b * mean_x - calc_a * mean_x2
    print(f'a={calc_a}; b={calc_b}; c={calc_c}')
    calcYPos = []
    x = 0
    it = []
    while x <= 15:
        calcYPos.append(takeY(x, calc_a, calc_b, calc_c, False))
        it.append(x)
        x+=step

    print(f'erro -> {takeY(15, calc_a, calc_b, calc_c, False) - 0}')

    plt.plot(iterations, yPositions, label="noise")
    plt.plot(it, calcYPos, label="quadratic regression")
    plt.show() 

if __name__ == "__main__":
    main()