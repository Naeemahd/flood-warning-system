from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run3():    
    centre = (52.2053, 0.1218)
    r = 10
    stations = build_station_list()
    count = stations_within_radius(stations,centre,r)
    print("Stations within radius:",count)
    return
run3()
