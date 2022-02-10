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

def test_stations_by_river():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    as_id = "test-s-id"
    am_id = "test-m-id"
    alabel = "some station"
    acoord = (-2.0, 4.0)
    atrange = (-2.3, 3.4445)
    ariver = "River X"
    atown = "My Town"
    acs = MonitoringStation(as_id, am_id, alabel, acoord, atrange, ariver, atown)
    test5 = (s, acs)
    testx = 'River X'#(river, ariver)
    test4 = stations_by_river(test5,testx)
    return test4