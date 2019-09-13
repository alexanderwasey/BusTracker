import json

from inky import InkyPHAT
from importconfig import importconfig 
from runloops import singlestop, multistops

def main(): 
    inky_display = InkyPHAT("black")
    inky_display.set_border(inky_display.WHITE)
    
    config = importconfig()

    
    if config['showtime'] == "True":
        showtime = True
    else: 
        showtime = False

#Need to work out the config mode
    if len(config["stops"]) > 1: 
        multistops(config, showtime, inky_display) 
    else: 
        stops = config["stops"][0]
        singlestop(stops, showtime, inky_display) 





if __name__ == "__main__":
    main()
