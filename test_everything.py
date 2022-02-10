
from floodsystem.geo import stations_by_distance

def test_stations_by_distance():
    list1 = ("1", "2", "3")
    p = (0,0)
    test1 = stations_by_distance(list1, p)