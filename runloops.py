import time 
import json 

from inky import InkyPHAT
from gettimes import getstopsinfo, sortUpcomingBuses 
from genimage import gensingleimage, genmultiimage, nothingtoshow, disptime

def singlestop(config, showtime, inky_display): 
    try: 
        IDs = config['IDs']
    except:
        print('Error loading config')
        print(config)
        return
    oldtimes = {}

    #Loop for displaying times 
    while True: 
        #Get the times for the stop 
        times = getstopsinfo(IDs)

        #Ensure that no more than 4 times are in the list
        if len(times) > 4: 
            times = times[0:4]
        times = sortUpcomingBuses(times)
        #Only update the screen if the times have changed and we have times to show
        if len(times) > 0:
            if (oldtimes != times):
                print('Attempt to gen image')
                img = gensingleimage(inky_display, times)
                inky_display.set_image(img)
                inky_display.show()
                oldtimes = times
            time.sleep(20)

            if showtime:
                print("Displaying time")
                img = disptime(inky_display)
                inky_display.set_image(img)
                inky_display.show()
                time.sleep(20)

        #If we have no times to show 
        else:
            print("No stops to show")
            img = nothingtoshow(inky_display)
            inky_display.set_image(img)
            inky_display.show() 
            time.sleep(60)
        
        

def multistops(config, showtime, inky_display):
    
    #Get number of stops to be displayed
    numstops = len(config['stops'])
    i = 0
    #Need to count the number of stops not shown to therefore know if all of our stops are currently not working 
    notshown = 0

    #Don't need to store old times as will always update every 20s 
    while True: 

        #Get the times for this stop 
        times = getstopsinfo(config['stops'][i]['IDs'])
        name = config['stops'][i]['name'] 
        #Ensure we only have 3 times  
        if len(times) > 3: 
            times = times[0:3]
        times = sortUpcomingBuses(times)
        #Only display if we have times to display 
        if len(times) > 0:  
            print('attempt to gen multi image for: ' + name)
        
            img = genmultiimage(inky_display, name, times)
            inky_display.set_image(img)
            inky_display.show()
            notshown = 0
            time.sleep(20)
        else: 
            print('No times to display for stop: ' + name)
            notshown += 1 
        
        #Check to see if all of our stops have nothing to show at the moment
        if (notshown >= numstops): 
            print("No stops to show")
            notshown = 0 
            img = nothingtoshow(inky_display)
            inky_display.set_image(img)
            inky_display.show() 
           
            #Refresh every minute to show the time
            time.sleep(60)
        
        
        #Iterate to the next stop
        i = i + 1 
        if (i >= numstops):
            i = 0
            #If we are showing the time do it at this point 
            if showtime: 
                print("Displaying time")
                img = disptime(inky_display)
                inky_display.set_image(img)
                inky_display.show()
                time.sleep(10)



