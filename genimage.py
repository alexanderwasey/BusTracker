from PIL import Image, ImageFont, ImageDraw
from inky import InkyPHAT
from font_fredoka_one import FredokaOne


#Create the image to be displayed on the hat
def genimage(display, stoptimes, todisplay):
    img = Image.new("P", (display.WIDTH, display.HEIGHT))
    draw = ImageDraw.Draw(img)
    
    #Load in the font
    f1 = ImageFont.truetype(FredokaOne,24)
    f2 = ImageFont.truetype(FredokaOne,16)
    f3 = ImageFont.truetype(FredokaOne,14)
    w, h = f1.getsize("Test") 

    #Counts where we are printing from
    printheight = 0
    
    stop = stoptimes[0]

    shown = 0
    #Print the times 
    for time in stop['times']:
        ttl = str(time['timeToLeave'])
        if (ttl == "0"):
            ttl = "DUE"
            
        if shown >= todisplay: 
            break

        #Print the service number
        draw.text((0,printheight), (str(time['serviceName'])), display.BLACK, f1)
        w, h = f1.getsize(str(time['serviceName']))
        printwidth = w

        #Print the service name in a smaller font
        #Need to pick the smaller font based on the length of the destination name 
        fs = f2
        if (len(time['destination']) > 14):
            fs = f3

        fsheight = printheight + int(0.25*h)
        draw.text((printwidth, fsheight), (" " + time['destination'] + ": "), display.BLACK, fs)
        w, h = fs.getsize(" " + time['destination'] + ": ")
        printwidth = w + printwidth  

        #Print the time to arrival
        draw.text((printwidth, printheight),ttl, display.BLACK, f1)
        w, h = f1.getsize(ttl)

        printheight += h
        shown += 1
          
    return img
