from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import relative_water_level_all

def run7():    
    # Create list with all the station data
    stations = build_station_list()
    update_water_levels(stations)
    stations = relative_water_level_all(stations)
    N=10
    stations_highest_rel_level(stations, N)
    return
run7()    
