
from floodsystem.geo import stations_by_distance

def test_stations_by_distance():
    list1 = ("(1,0)", "(1,0)", "(1,0)")
    p = (0,0)
    test1 = stations_by_distance(list1, p)