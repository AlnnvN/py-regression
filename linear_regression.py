import matplotlib.pyplot as plt
import math
import numpy as np
from numpy import random

def takeY(x: float, a: float, b: float, noise: float = False) -> float:

    y = (a*x + b)

    if noise:
        return random.normal(loc=y, scale=0.05)
    else:
        return y
    

def main():
    y_linear_positions = []
    iterations = []
    step = 0.01

    x = 1
    while x <= 2:
        y = takeY(x, 1, 2, True)

        y_linear_positions.append(y)

        iterations.append(x)

        x+=step

    x_array = np.array(iterations)
    y_array = np.array(y_linear_positions)

    mean_x = x_array.mean()
    mean_y = y_array.mean()

    x_minus_mean = np.array(x_array - mean_x)
    y_minus_mean = np.array(y_array - mean_y)

    sxy = np.array(x_minus_mean * y_minus_mean).sum()
    sxx = np.array(x_minus_mean * x_minus_mean).sum()

    calc_b = sxy / sxx

    calc_a = mean_y - (calc_b * mean_x)

    print(f'a={calc_a}; b={calc_b};')
    y_linear_regression = []
    regression_iterations = []
    x = 1
    while x <= 15:
        y = takeY(x, calc_b, calc_a, False)

        y_linear_regression.append(y)

        regression_iterations.append(x)
        x+=step

    plt.plot(iterations, y_linear_positions, label="linear_noise")
    plt.plot(regression_iterations, y_linear_regression, label="linear_regression")
    plt.legend()
    plt.show() 

if __name__ == "__main__":
    main()