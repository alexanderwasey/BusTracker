import json

from inky import InkyPHAT
from importconfig import importconfig 
from runloops import singlestop, multistops

def main(): 
    inky_display = InkyPHAT("black")
    inky_display.set_border(inky_display.WHITE)
    
    config = importconfig()
    #Need to work out the config mode
    if len(config["stops"]) > 1: 
        multistops(config, inky_display) 
    else: 
        stops = config["stops"][0]
        if config['showtime'] == "True":
            showtime = True
        else: 
            showtime = False
        singlestop(stops, showtime, inky_display) 





if __name__ == "__main__":
    main()
