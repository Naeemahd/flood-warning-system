# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit
def stations_by_distance(list_coord, p):
    # Create an empty list, to be populated by the distances generated from the haversine function
    list_distance = []
    for i in range (len(list_coord)):
        # For each item in the list of coordinates, find the distance between p and the coordinates
        d = haversine(list_coord[i],p)
        list_distance.append(d)  
    return list_distance
   
def build_lists(stations,p):
    #The below loop creates 3 lists, one for each of the Station names, Closest town and their coordinates
    list_names=[]
    list_towns=[]
    list_coord=[]
    for i in range(len(stations)):
        #This loop breaks up the "stations" function and creates three seperate lists for each attribute
        list_names.append(stations[i].name)
        list_towns.append(stations[i].town)
        list_coord.append(stations[i].coord)
    #This then runs the function above and finds the distance from the point
    list_distance = (stations_by_distance(list_coord, p))
    
    #Then merges the three lists into a list of tuples
    list_tuple = list(zip(list_names, list_towns, list_distance))
    return list_tuple
def stations_within_radius(stations, centre, r):
    list_tuple = build_lists(stations,centre)
    #now sort list of tuples by the 3rd part - distance
    list_tuple.sort(key=lambda x:x[2])
    count_of_stations = 0
    for i in range(len(list_tuple)):
        tuple = (list_tuple[i])
        if(tuple[2]<r):
            count_of_stations += 1
    return count_of_stations
