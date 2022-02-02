'''print number of stuff in set and first 10 alphbetical'''

from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list

def run3():    
    stations = build_station_list()
    list = rivers_with_station(stations)
    print("Number of Rivers:",len(list))
    print(list[:10])
    return

run3()
