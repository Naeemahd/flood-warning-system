import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    
    x = matplotlib.dates.date2num(dates)

    # Create set of 10 data points on interval (0, 2)
   
    x_c = x
    y = levels
    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(x_c-x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)
    return poly, x[0], x_c
