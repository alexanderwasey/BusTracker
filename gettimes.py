import urllib.request 
import json

#Get the sorted list of departures from multiple stops
def getstopsinfo(stops):
    upcomingBuses = list()
    for stop in stops: 
        stopinfo = getstopinfo(stop)
        #Check that the json was returned correctly
        if "stop_id" in stopinfo.keys():
            services = extractbasicinfo(stopinfo)
            upcomingBuses = upcomingBuses + services
    
    #Now sort
    return filterUpcomingBuses(sortUpcomingBuses(upcomingBuses))

#Gets the json for information about a stop from the tfeapp webpage
def getstopinfo(stopNo):
    
    stopInfo = {}

    try:
        URL = 'https://tfeapp.com/api/Unified.3.0/departure_boards.php?stops=' + str(stopNo)
    
        html = urllib.request.urlopen(URL)
        jsonstring = html.read()
        stopInfo = json.loads(jsonstring)[0]
        
    except: 
        print("Stop " + str(stopNo) + ": data unable to be found \n")
    
    return stopInfo

#For each upcoming bus for a stop returns 
# Number + Destination + Time until arrival + If diverted
def extractbasicinfo(stopInfo):
    upcomingBuses = list()

    try:
        #Need to iterate over the json structure - iterate over each service
        for service in stopInfo["services"]: 
            serviceName = service["service_name"]
            #For each upcoming departure 
            for upcomingBus in service["departures"]:
                upcoming = {}
                upcoming['serviceName'] = serviceName
                upcoming['destination'] = upcomingBus["destination"]
                upcoming['timeToLeave'] = upcomingBus["minutes"]
                upcoming['diverted'] = upcomingBus["diverted"]

                upcomingBuses.append(upcoming)
    except: 
        print("Error parsing json")
 
    return upcomingBuses

#Extracts time to leave from json 
def extractTimeToLeave(json):
    try: 
        return int(json["timeToLeave"])
    except: 
        return 10080 #In case of error this ensure that the service will not show up - 7 days from now.

#Sorts the upcoming buses in order of next to arrive 
def sortUpcomingBuses(upcomingBuses):
    upcomingBuses.sort(key=extractTimeToLeave)
    return upcomingBuses

#Remove duplicate services
def filterUpcomingBuses(upcomingBuses):
    alreadySeen = list() 
    nonduplicates = list() 
    duplicates = list()

    for bus in upcomingBuses: 
        busSignature = {}
        busSignature['route'] = bus['serviceName']
        busSignature['desintation'] = bus['destination']
        
        #Only show if arriving in next 2 hours 
        if bus['timeToLeave'] <= 120:
            if busSignature not in alreadySeen: 
                alreadySeen.append(busSignature)
                nonduplicates.append(bus)
            else: 
                duplicates.append(bus)
    #Have none duplicated buses first followed by duplicated buses
    return nonduplicates + duplicates
