import matplotlib.pyplot as plt
import numpy as np
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    typical_range = station.typical_range
    high = typical_range[1]
    low = typical_range[0]
    typical_high = []
    typical_low = []
    for i in range(len(levels)):
        typical_high.append(high)
        typical_low.append(low)

    plt.plot(dates, levels, label = "Water Level")
    plt.plot(dates,typical_high, label = "Typical High", linestyle = "--")
    plt.plot(dates,typical_low, label = "Typical Low", linestyle = "--")


    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend()

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
    return

def plot_water_level_with_fit(station, dates, levels, p):
    typical_range = station.typical_range
    high = typical_range[1]
    low = typical_range[0]
    typical_high = []
    typical_low = []
    for i in range(len(levels)):
        typical_high.append(high)
        typical_low.append(low)

    poly, d0, x = polyfit(dates, levels, p)
    
    # Plot original data points
    #plt.plot(dates, y, '.')

    # Plot polynomial fit at 30 points along interval
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - x[0]), label = "Polynomial")

    plt.plot(dates, levels, label = "Water Level")
    plt.plot(dates,typical_high, label = "Typical High", linestyle = "--")
    plt.plot(dates,typical_low, label = "Typical Low", linestyle = "--")


    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend()

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
    return
