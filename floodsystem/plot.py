import matplotlib.pyplot as plt

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
