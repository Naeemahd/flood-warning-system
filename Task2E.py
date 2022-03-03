from floodsystem.station import relative_water_level_all
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level_with_historical, stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels

import datetime

def run2E():
# Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    stations = relative_water_level_all(stations)

    N = 5

    flood_risk_stations = stations_highest_rel_level(stations,N)
    # Make a list of the names of the 5 stations that currently have the greatest relative water level
    # For each of those stations, get the data from the last 10 days
    # Plot the water levels for each 

    dt = 10

    for i in range(len(flood_risk_stations)):
        station = flood_risk_stations[i]
        station_name = station[0]
        for j in range(len(stations)):
            if stations[j].name == station_name:
                dates, levels = fetch_measure_levels(
                stations[j].measure_id, dt=datetime.timedelta(days=dt))
                if dates == [] or levels == []:
                    print("No historical data available for the current station: {}".format(stations[j].name))
                else:
                    plot_water_levels(stations[j], dates, levels)
    return
# Fetch data over past 10 days
    
run2E()
