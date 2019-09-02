from PIL import Image, ImageFont, ImageDraw
from inky import InkyPHAT
from font_fredoka_one import FredokaOne
from acronym import acronym

#Create the image to be displayed on the hat
def gensingleimage(display, times):
    img = Image.new("P", (display.WIDTH, display.HEIGHT))
    draw = ImageDraw.Draw(img)
    
    #Load in the font
    f1 = ImageFont.truetype(FredokaOne,25)
    f2 = ImageFont.truetype(FredokaOne,16)

    gentimes(0, draw, display, times, f1, f2)

    return img

def genmultiimage(display, name, times):
    img = Image.new("P", (display.WIDTH, display.HEIGHT))
    draw = ImageDraw.Draw(img)
    
    #Load in the font
    f1 = ImageFont.truetype(FredokaOne,25)
    f2 = ImageFont.truetype(FredokaOne,16)

    #First print the name of the stop
    draw.text((0, 0), name, display.BLACK, f1)
    w, h = f1.getsize(name)
    #Underline the text
    draw.line([(3,h),(w - 3,h)], display.BLACK, 2)


    gentimes(h, draw, display, times, f1, f2)

    return img

def gentimes(printheight, draw, display, times, f1, f2):
    #Now need to print the stops
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
        destination = acronym(destination)


        f2height = printheight + int(0.25*h)
        draw.text((printwidth, f2height), (" " + destination + ": "), display.BLACK, f2)
        w, h = f2.getsize(" " + destination + ": ")
        printwidth = w + printwidth  

        #Print the time to arrival
        draw.text((printwidth, printheight),ttl, display.BLACK, f1)
        w, h = f1.getsize(ttl)

        printheight += h
    
def nothingtoshow(display): 
    img = Image.new("P", (display.WIDTH, display.HEIGHT))
    draw = ImageDraw.Draw(img) 
    f1 = ImageFont.truetype(FredokaOne,22)

    #Gen the text
    draw.text((15,30), "No buses to show", display.BLACK, f1)

    return img


