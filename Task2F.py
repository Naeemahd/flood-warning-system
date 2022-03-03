from floodsystem.analysis import polyfit
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import relative_water_level_all
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
import matplotlib.pyplot as plt


dt = 10
p = 20
N = 5
stations = build_station_list()
update_water_levels(stations)
stations = relative_water_level_all(stations)

flood_risk_stations = stations_highest_rel_level(stations,N)

for i in range(len(flood_risk_stations)):
    # Find station
    flood_station =  flood_risk_stations[i]
    station_name = flood_station[0]
    for j in range(len(stations)):
        if stations[j].name == station_name:
            dates, levels = fetch_measure_levels(
            stations[j].measure_id, dt=datetime.timedelta(days=dt))
            if dates == [] or levels == []:
                print("No historical data available for the current station: {}".format(stations[j].name))
            else:
                plot_water_level_with_fit(stations[j], dates, levels, p)
