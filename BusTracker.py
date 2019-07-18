import json

from inky import InkyPHAT
from importconfig import importconfig 
from singlestop import singlestop

def main(): 
    inky_display = InkyPHAT("black")
    inky_display.set_border(inky_display.WHITE)
    
    config = importconfig()
    #Need to work out the config mode
    if len(config['stops']) > 1: 
        print("Not supported at this time")
    else: 
        config = config['stops'][0]
        singlestop(config, inky_display) 





if __name__ == "__main__":
    main()
