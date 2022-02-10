from floodsystem.geo import stations_by_distance,build_lists

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