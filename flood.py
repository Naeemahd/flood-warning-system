def stations_highest_rel_level(stations, N):
    #create empty lists
    level = []
    names=[]
    #loops through stations list and add the names and water levels
    for i in range(len(stations)):
        level.append(stations[i].latest_level)
        names.append(stations[i].name)
    #puts lists together    
    list_tuple = list(zip(names, level))    
    #sorts list by water level low to high
    list_tuple.sort(key= lambda x:x[1])  
    #print last N terms of list_tuple 
    for i in range(N):
        print(list_tuple[(-1*i)-1]) 
