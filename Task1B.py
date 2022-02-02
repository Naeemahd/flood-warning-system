from floodsystem.stationdata import build_station_list
from floodsystem.geo import build_lists

def run2():
    # Build list of stations
    stations = build_station_list()
    
    #P is the defined point that the distance is found from
    p = (52.2053,0.1218)
    # Build_lists creates three lists - one for each: names, towns, coordinates
    # It then uses the haversine formula to find the distance from point p (defined in geo)
    # Then it forms a list of tuples (Name, Town, Distance) - defined list_tuple
    list_tuple = build_lists(stations,p)    
    #now sort list of tuples by the 3rd part - distance
    list_tuple.sort(key=lambda x:x[2])
    
    print("First 10: ",list_tuple[:10])
    
    print("Last 10: ",list_tuple[-10:])
    return
run2()
