from floodsystem.station import relative_water_level_all
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import relative_water_level_all
from floodsystem.flood import stations_level_over_threshold

def run2B():
# Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    stations = relative_water_level_all(stations)
    tol = 0.8
    print(stations_level_over_threshold(stations,tol))
    return

run2B()
