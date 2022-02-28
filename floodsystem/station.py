# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data
"""

from pickle import FALSE
from tkinter import TRUE

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town
        self.check = 0 ################################### MODIFIED ########################################

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}\n".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        # Get typical range attribute from item
        for i in range(len(self)):
            # Assign a boolean variable - if it passes all tests, will be assigned TRUE else FALSE
            # Test typical range values
            check = TRUE
            test = self[i].typical_range
            if test == None:
                check = FALSE
            elif test[0]>test[1]:
                check = FALSE
            #elif test[0]<0:
            #    check = FALSE
            setattr(self[i],"check",check)
        # If all tests are passed then check = TRUE
        # log new attribute to item called "check" - that reads true or false
        
        return
    #For Task 2B
    def relative_water_level(self):
            
        for i in range(len(self)):
            # get the typical range and define the low and high points
            typical_range = self[i].typical_range
            height = self[i].latest_level 
            if typical_range == None:
                fraction = None
            elif height == None:
                fraction = None
            else:
                low = typical_range[0]
                high = typical_range[1]
                # Calculate the relative water level
                fraction = (height-low)/(high-low)
            setattr(self[i],"fraction",fraction)
        return

def inconsistent_typical_range_stations(stations):
    MonitoringStation.typical_range_consistent(stations)
    error_list = []

    for i in range(len(stations)):
        if stations[i].check == FALSE:
            error_list.append(stations[i].name)
    return error_list
    
def relative_water_level_all(stations):
    MonitoringStation.relative_water_level(stations)
    return stations
