from floodsystem.analysis import polyfit
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import matplotlib.pyplot as plt
from floodsystem.plot import plot_water_level_with_fit


dt = 10
stations = build_station_list()

# Station name to find
station_name = "Hayes Basin"

# Find station
station_cam = None
for station in stations:
    if station.name == station_name:
        station_cam = station
        break

dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=datetime.timedelta(days=dt))
p = 20                                    
poly, d0 = polyfit(dates, levels, p)
print(poly)
print(d0)
plot_water_level_with_fit(station, dates, levels, p)