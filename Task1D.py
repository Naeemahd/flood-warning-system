'''print number of stuff in set and first 10 alphbetical'''

from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list

#This function is for part a - returning a list of all the rivers
def run4a():    
    stations = build_station_list()
    list_rivers = rivers_with_station(stations)
    print("Number of Rivers:",len(list_rivers))
    print(list_rivers[:10])
    return

#This function is for part b - returning the names of stations on given rivers
def run4b():
    #Define the search list of rivers here
    river = ["River Aire","River Cam","River Thames"]
    stations = build_station_list()
    #For each river in the search list
    for i in range(len(river)):
        #Find the stations along that river
        string = stations_by_river(stations,river[i])
        #Print the number of stations and the list (already sorted alphabetically)
        print("Stations by {}: {}".format(river[i],len(string)))
        print(string)
    return

run4a()
run4b()
