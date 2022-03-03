import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def plot_water_level_with_fit(station, dates, levels, p):

    x = matplotlib.dates.date2num(dates)

    x_c = x
    y = levels
    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x_c-x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    # Plot original data points
    plt.plot(x_c, y, '.')

    # Plot polynomial fit at 30 points along interval
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - x[0]))

    # Display plot
    plt.show()