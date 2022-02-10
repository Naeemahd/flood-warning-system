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

#TASK 1D
#Returns an alphabetical list of all the rivers with stations
def rivers_with_station(stations):
    #Make a blank set to fill
    rws = set()
    for i in range(len(stations)):
        #Loop through each station and add the river, no duplicates will be added
        rws.add(stations[i].river)
    #Now sort the set, sorted returns it alphabetically
    rws = sorted(rws) 
    return rws
   
#Returns a list of stations on any given river
def stations_by_river(stations,testriver):
    #Create an empty list called String 
    string = []
    #For each station item, get the river and the name
    #If the river matches the given river then add it to the list
    for i in range(len(stations)): 
        test=stations[i].river
        name=stations[i].name
        if test == testriver:
            string.append(name)
    #Now sort the list alphabetically
    string = sorted(string)
    return string

#task 1E

#make list of river names and station number ordered in number of stations- return greatest N
def rivers_by_station_number(stations,N):
    # Make a list of the river names
    list_rivers = rivers_with_station(stations)
    # Make an empty list for the count of stations
    list_count = []
    # For each river, find the number of stations
    for i in range(len(list_rivers)):
        river = list_rivers[i]
        # Reset count for each new river
        count = 0
        # Loop through list of all the stations, adding to the count for each river match
        for j in range(len(stations)): 
            test=stations[j].river
            if test==river:
                count += 1
        # When count is finished for each river, add the number to the list of counts
        list_count.append(count)
 
    # Make a dictionary of the river names and number of stations
    dict_riverscount = dict(zip(list_rivers,list_count))
    # Sort the dictionary by rivers with most stations first
    sort_dict = sorted(dict_riverscount.items(), key=lambda x: x[1], reverse=True)
    # Sort the list of count of stations (so it matches the dictionary) 
    list_count.sort(reverse=True)
    # Check if the Nth item and the Nth +1 item have the same count (if so then they are ==Nth and should both be included)
    # Use an iterative function to check that all Nth= terms have been found
    # This function will define a new N that includes all Nth= terms
    N = n_equal_check(list_count,N)
    # Return the first N items
    return sort_dict[:N]

# This function is part of Task1E, it is a recursion to find all Nth equal terms
def n_equal_check(list_count, N):
    # It finds the Nth and Nth+1 terms and checks if their count is the same
    if list_count[N-1]==list_count[N]:
        #If count is the same, then it adds 1 to the value of N stored and calls the function again
        N +=1
        N = n_equal_check(list_count,N)
    return N
  
