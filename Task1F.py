from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def run6():    
    # Create list with all the station data
    stations = build_station_list()
    
    list1 = sorted(inconsistent_typical_range_stations(stations))
    # Call inconsistent_typical_range_stations which loops through the list of stations and 
    # returns a list of all stations with inconsistent or missing data
    # Sort alphabetically
    print(list1)
    #print(len(list1))
    return 
run6()