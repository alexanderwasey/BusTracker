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
        IDs = config['IDs']
    except:
        print('Error loading config')
        return

    
    #Loop for displaying times 
    while True: 
        #Get the times for the stop 
        times = getstopsinfo(IDs)

        #Ensure that no more than 4 times are in the list
        if len(times) > 4: 
            times = times[0:3]


        print('Attempt to gen image')
        img = genimage(inky_display, times)
        inky_display.set_image(img)
        inky_display.show()
    
        time.sleep(20)




if __name__ == "__main__":
    main()
