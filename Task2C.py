from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import relative_water_level_all

def run7():    
    # Create list with all the station data
    stations = build_station_list()
    update_water_levels(stations)
    stations = relative_water_level_all(stations)
    N=10
    list_tuple = stations_highest_rel_level(stations, N)
    
    for i in range(N):
        print("Station name and relative level: {}, {}".format(
                list_tuple[i][0], list_tuple[i][1]))
    #print last N terms of list_tuple 
    return
run7()    
