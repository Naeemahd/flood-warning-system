def stations_highest_rel_level(stations, N):
    high_level = []
    names=[]
    for i in range(len(stations)):
        high_level.append(stations[i].latest_level)
        names.append(stations[i].name)
    list_tuple = list(zip(names, high_level))    
    list_tuple.sort(key= lambda x:x[1])  
    #return list_tuple 
    for i in range(N):
        print(list_tuple[i]) 
