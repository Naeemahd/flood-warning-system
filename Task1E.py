from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run5():    
    # Create list with all the station data
    stations = build_station_list()
    # Define N here, the number of top rivers to return
    N = 9
    print("Top {} rivers with most stations: {}".format(N,rivers_by_station_number(stations,N)))
    return

run5()
