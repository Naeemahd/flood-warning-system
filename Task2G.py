from floodsystem.analysis import polyfit
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import relative_water_level_all
from floodsystem.flood import stations_highest_rel_level
import matplotlib.pyplot as plt


dt = 2
N = 75
stations = build_station_list()
update_water_levels(stations)
stations = relative_water_level_all(stations)

flood_risk_stations = stations_highest_rel_level(stations,N)

flood_towns = []

for i in range(len(flood_risk_stations)):
    # Find station
    flood_station =  flood_risk_stations[i]
    station_name = flood_station[0]
    for j in range(len(stations)):
        if stations[j].name == station_name:
            flood_towns.append(stations[j].town)


for k in range(len(flood_towns)):
    test_town = []
    risk_factor = 0
    count = 0
    town_risk = 0 
    
    if flood_towns[k] == None:
        pass
    for l in range(len(stations)):
        if stations[l].town == flood_towns[k]:
            dates, levels = fetch_measure_levels(
            stations[l].measure_id, dt=datetime.timedelta(days=dt))
            if len(levels) > 1:
                if levels[0]<levels[-1] and stations[l].fraction > 2:
                    test_town.append("Severe")
                    risk_factor += 4

                elif (levels[0]< levels[-1] and stations[l].fraction > 1.4) or (stations[l].fraction > 2):
                    test_town.append("High")
                    risk_factor += 3
                    
                elif (levels[0]< levels[-1] and stations[l].fraction > 1) or (stations[l].fraction > 1.4):
                    test_town.append("Moderate")
                    risk_factor += 2
                    
                else:
                    test_town.append("Low")
                    risk_factor += 1
    if len(test_town) != 0:
        town_risk = risk_factor/len(test_town)
    if town_risk > 2.5:
        town_risk_rating = "Severe - run / swim for your lives!!"
    elif town_risk > 1.9: 
        town_risk_rating = "High - don't forget your swimming costumes!"
    elif town_risk > 1:
        town_risk_rating = "Moderate - welly boots should be fine"
    else: 
        town_risk_rating = "Low"   
    print("Flood Risk Warning: {} Status: {}".format(flood_towns[k], town_risk_rating))

'''

        if stations[j].name == station_name:
            dates, levels = fetch_measure_levels(
            stations[j].measure_id, dt=datetime.timedelta(days=dt))
            if dates == [] or levels == []:
                print("No historical data available for the current station: {}".format(stations[j].name))
            else:
                plot_water_levels_with_poly(stations[j], dates, levels,)
'''