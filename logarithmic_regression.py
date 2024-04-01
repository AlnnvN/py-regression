import matplotlib.pyplot as plt
import math
import numpy as np
from numpy import random
import csv
    
def takeYLn(x: float, a: float, b: float, noise: float = False) -> float:

    y = a * math.log(x) + b
 
    if noise:
        return random.normal(loc=y, scale=0.3)
    else:
        return y

def main():
    file = open('data.csv')
    data = csv.reader(file, delimiter=',')

    y_log_positions = []
    iterations = []
    step = 0.01
    max_iterations = 50
    slice_position = int(10 // step)

    a_noise = 1
    b_noise = 1

    for row in data:
        y_log_positions.append(float(row[1]))
        iterations.append(float(row[0]))

    initial = y_log_positions[0]
    for i in range(len(y_log_positions)):
        y_log_positions[i]-=initial
        print(y_log_positions[i])

    print("\n\n")

    initial_time = iterations[0]
    for i in range(len(iterations)):
        iterations[i]-=initial_time
        iterations[i]+=1
        print(iterations[i])
    

    for i in range(len(y_log_positions)):
        print(f'[{iterations[i]}, {y_log_positions[i]}]')

    # x = 1
    # while x <= max_iterations:
    #     y = takeYLn(x, a_noise, b_noise, True)
    #     y_log_positions.append(y)

    #     iterations.append(x)

    #     x+=step

    y_array = np.array(y_log_positions)
    x_array = np.array(iterations)

    sum_ln_x = np.array(np.log(x_array)).sum()
    sum_y_ln_x= np.array(y_array * np.log(x_array)).sum()
    sum_y = y_array.sum()
    sum_ln_x_2 = np.array(np.power(np.log(x_array), 2)).sum()
    n = len(x_array)

    calc_b = (n * sum_y_ln_x - sum_y * sum_ln_x) / (n * sum_ln_x_2 - np.power(sum_ln_x, 2))

    calc_a = ((sum_y - calc_b * sum_ln_x)) / n
    
    print(f'a={calc_b}; b={calc_a};')
    y_log_regression = []
    regression_iterations = []
   
    step = 0.04
    x = iterations[0]
    print(f"start time {x}, end time {iterations[-1] + 10}")
    while x <= iterations[-1] + 10:
        y_log_regression.append(takeYLn(x, calc_b, calc_a, False))

        regression_iterations.append(x)
        x+=step

    plt.plot(iterations, y_log_positions, label="logarithmic_noise")
    plt.plot(regression_iterations, y_log_regression, label="logarithmic_regression")
    plt.legend()
    plt.show() 

if __name__ == "__main__":
    main()