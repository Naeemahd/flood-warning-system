def stations_highest_rel_level(stations, N):
    #create empty lists
    rel_level = []
    names=[]

    #loops through stations list and add the names and water levels
    for i in range(len(stations)):
        
        if str(stations[i].latest_level) != None:
            rel_level.append(stations[i].fraction)
            names.append(stations[i].name)
          
    #puts lists together    
    list_tuple = list(zip(names,rel_level))    
    #sorts list by water level low to high
    list_tuple.sort(key= lambda x:x[1], reverse = True)  

    for i in range(N):
        print("Station name and relative level: {}, {}".format(
                list_tuple[i][0], list_tuple[i][1]))
    #print last N terms of list_tuple 
    
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
