from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run7():    
    # Create list with all the station data
    stations = build_station_list()
    update_water_levels(stations)
    N=10
    stations_highest_rel_level(stations, N)
    return
run7()    