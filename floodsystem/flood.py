from floodsystem.datafetcher import fetch_measure_levels

import datetime

def stations_highest_rel_level(stations, N):
    #create empty lists
    rel_level = []
    names=[]

    #loops through stations list and add the names and water levels
    for i in range(len(stations)):
        
        if stations[i].fraction != None:
            if str(stations[i].latest_level) != None:
                rel_level.append(stations[i].fraction)
                names.append(stations[i].name)
            
    #puts lists together    
    list_tuple = list(zip(names,rel_level))    
    #sorts list by water level low to high
    list_tuple.sort(key= lambda x:x[1], reverse = True)  
    return list_tuple[:N]

##### THE BELOW FUNCTION IS NOT IN USE BUT COULD BE USED TO CORRECT TASK 2E #######
def stations_highest_rel_level_with_historical(stations, N):
    #create empty lists
    rel_level = []
    names=[]
    dt = 1

    #loops through stations list and add the names and water levels
    for i in range(len(stations)):
        
        if stations[i].fraction != None:
            if str(stations[i].latest_level) != None:
                dates, levels = fetch_measure_levels(
                stations[i].measure_id, dt=datetime.timedelta(days=dt))
                if dates == [] or levels == []:
                    print("No historical data available for the current station: {}".format(stations[j].name))
                else:
                    rel_level.append(stations[i].fraction)
                    names.append(stations[i].name)
    #puts lists together    
    list_tuple = list(zip(names,rel_level))    
    #sorts list by water level low to high
    list_tuple.sort(key= lambda x:x[1], reverse = True)  
    return list_tuple[:N]
    
def stations_level_over_threshold(stations, tol):
    over_tol = []
    rel_level =[]
    for i in range(len(stations)):
        if stations[i].fraction != None and str(stations[i].latest_level != None):
            if stations[i].fraction > tol:
                over_tol.append(stations[i].name)
                rel_level.append(stations[i].fraction)
    list_tuple = list(zip(over_tol,rel_level))    
    list_tuple.sort(key= lambda x:x[1], reverse = True)   
    return(list_tuple)
        
