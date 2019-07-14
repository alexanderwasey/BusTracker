from PIL import Image, ImageFont, ImageDraw
from inky import InkyPHAT
from font_fredoka_one import FredokaOne
from acronym import acronym

#Create the image to be displayed on the hat
def genimage(display, times):
    img = Image.new("P", (display.WIDTH, display.HEIGHT))
    draw = ImageDraw.Draw(img)
    
    #Load in the font
    f1 = ImageFont.truetype(FredokaOne,25)
    f2 = ImageFont.truetype(FredokaOne,16)
    w, h = f1.getsize("Test") 

    #Counts where we are printing from
    printheight = 0

    #Print the times 
    for time in times:
        ttl = str(time['timeToLeave'])
        if (ttl == "0"):
            ttl = "DUE"
            
        #Print the service number
        draw.text((0,printheight), (str(time['serviceName'])), display.BLACK, f1)
        w, h = f1.getsize(str(time['serviceName']))
        printwidth = w
        
        #Check destination name isn't too long
        destination = time['destination']
        if (len(destination) > 14):
                destination = acronym(destination)


        f2height = printheight + int(0.25*h)
        draw.text((printwidth, f2height), (" " + destination + ": "), display.BLACK, f2)
        w, h = f2.getsize(" " + destination + ": ")
        printwidth = w + printwidth  

        #Print the time to arrival
        draw.text((printwidth, printheight),ttl, display.BLACK, f1)
        w, h = f1.getsize(ttl)

        printheight += h
          
    return img
