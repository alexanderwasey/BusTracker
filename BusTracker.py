import time

from inky import InkyPHAT
from importconfig import importconfig 
from gettimes import getstopsinfo
from genimage import genimage


def main(): 
    inky_display = InkyPHAT("black")
    inky_display.set_border(inky_display.WHITE)
    
    config = importconfig()
    
    try: 
        stops = config['stops']
        toDisplay = config['toDisplay']
    except:
        print('Error loading config')
        return

    
    #Loop for displaying times 
    while True: 
        #Will need to collect times for each stop and connect them with stop name to send to the display.
        stopstimes = list()
        for stop in stops: 
            times = getstopsinfo(stop['IDs'])
            stoptime = {}
            stoptime['times'] = times 
            stoptime['name'] = stop['name']
            stopstimes.append(stoptime)

        print('Attempt to gen image')
        img = genimage(inky_display, stopstimes, toDisplay, inky_display.HEIGHT, inky_display.WIDTH)
        inky_display.set_image(img)
        inky_display.show()
    
        time.sleep(30)




if __name__ == "__main__":
    main()
