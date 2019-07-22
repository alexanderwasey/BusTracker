import time 
import json 

from inky import InkyPHAT
from gettimes import getstopsinfo 
from genimage import gensingleimage, genmultiimage

def singlestop(config, inky_display): 
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

        #Only update the screen if the times have changed
        if (oldtimes != times):
            print('Attempt to gen image')
            img = gensingleimage(inky_display, times)
            inky_display.set_image(img)
            inky_display.show()
            oldtimes = times
    
        time.sleep(20)


def multistops(config, inky_display):
    
    #Get number of stops to be displayed
    numstops = len(config['stops'])
    i = 0

    #Don't need to store old times as will always update every 20s 

    while True: 

        #Get the times for this stop 
        times = getstopsinfo(config['stops'][i]['IDs'])
        name = config['stops'][i]['name'] 
        #Ensure we only have 3 times  
        if len(times) > 3: 
            times = times[0:3]
        
        print('attempt to gen multi image')
        
        img = genmultiimage(inky_display, name, times)
        inky_display.set_image(img)
        inky_display.show()

        i = i + 1
        if (i >= numstops):
            i = 0
        time.sleep(30)        
