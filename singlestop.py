import time 
import json 

from inky import InkyPHAT
from gettimes import getstopsinfo 
from genimage import gensingleimage


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
