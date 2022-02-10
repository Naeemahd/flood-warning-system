from floodsystem.geo import stations_by_distance,build_lists,rivers_with_station,stations_by_river
from floodsystem.station import MonitoringStation

def test_stations_by_distance():
    list1 =((1,0), (1,0), (1,0))
    p = (0,0)
    test1 = stations_by_distance(list1, p)
    

def test_build_lists():
    #The below loop creates 3 lists, one for each of the Station names, Closest town and their coordinates
    list_names=["test", "Test", "TEst"]
    list_towns=["test", "Test", "TEst"]
    list_coord=[(1,0), (1,0), (1,0)]
    p = (0,0)
    #This then runs the function above and finds the distance from the point
    list_distance = (stations_by_distance(list_coord, p))  

def tes_rivers_with_station():
 
    rws = set('apple', 'orange', 'apple', 'pear', 'orange', 'banana')
    
    rws = sorted(rws) 
    assert rws == ('apple', 'banana', 'pear', 'orange')

s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (-2.0, 4.0)
trange = (-2.3, 3.4445)
river = "River X"
town = "My Town"
s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)


def test_stations_by_river():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    test4 = stations_by_river(s, "River X")
    assert test4 == ['test-s-id']