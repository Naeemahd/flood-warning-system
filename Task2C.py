from floodsystem.flood import stations_highest_rel_level

def run7():    
    # Create list with all the station data
    stations = build_station_list()
    N=10
    stations_highest_rel_level(stations, N)
    return
run7()    